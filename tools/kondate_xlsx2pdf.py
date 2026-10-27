#!/usr/bin/env python3
"""ヨシケイキッチン 献立表 Excel → コース別PDF
usage: python3 -I kondate_xlsx2pdf.py IN.xlsx OUTDIR
- シートごとに1コース（シート名「献立表（簡単）」やタイトル「11/9週<簡単おかず>週間献立表」から判定）
- 変換前に作業コピーの XML を修正：MSゴシック→IPAゴシック（行の高さを Excel と揃える）、各シートを1ページに収める
- 出力: OUTDIR/YYYY-MM-DD_<key>.pdf （日付はその週の月曜）
- 最後に JSON で {start, files:{key: 'pdf/…'}} を表示
"""
import sys, os, re, json, shutil, subprocess, tempfile, datetime, zipfile
import openpyxl
from pypdf import PdfReader

COURSES = [  # 判定順：長い名前から
    ('ボリューム', 'volume'), ('ﾎﾞﾘｭｰﾑ', 'volume'), ('超簡単プラス', 'chokantanplus'), ('超簡単', 'chokantan'),
    ('簡単', 'kantan'), ('手づくり', 'tezukuri'), ('手作り', 'tezukuri'),
]
FONTS = [('ＭＳ Ｐゴシック', 'IPAPGothic'), ('ＭＳ ゴシック', 'IPAGothic'), ('MS PGothic', 'IPAPGothic'), ('MS Gothic', 'IPAGothic')]

def course_of(text):
    for k, v in COURSES:
        if k in text: return v
    return None

def monday(m, d, today=None):
    today = today or datetime.date.today()
    best = None
    for y in (today.year - 1, today.year, today.year + 1):
        try: c = datetime.date(y, m, d)
        except ValueError: continue
        if best is None or abs((c - today).days) < abs((best - today).days): best = c
    return best

def fix_sheet(s):
    # 1ページに収める
    if re.search(r'<sheetPr\b', s):
        if 'fitToPage' in s:
            s = re.sub(r'fitToPage="0"', 'fitToPage="1"', s)
        elif re.search(r'<sheetPr\b[^>]*/>', s):
            s = re.sub(r'<sheetPr\b([^>]*)/>', r'<sheetPr\1><pageSetUpPr fitToPage="1"/></sheetPr>', s, count=1)
        elif '<pageSetUpPr' in s:
            s = re.sub(r'<pageSetUpPr\b', '<pageSetUpPr fitToPage="1"', s, count=1)
        else:
            s = re.sub(r'(<sheetPr\b[^>]*>)', r'\1<pageSetUpPr fitToPage="1"/>', s, count=1)
    else:
        s = re.sub(r'(<worksheet\b[^>]*>)', r'\1<sheetPr><pageSetUpPr fitToPage="1"/></sheetPr>', s, count=1)
    def ps(m):
        t = re.sub(r'\s(scale|fitToWidth|fitToHeight)="[^"]*"', '', m.group(0))
        return t.replace('<pageSetup', '<pageSetup fitToWidth="1" fitToHeight="1"', 1)
    return re.sub(r'<pageSetup\b[^>]*>', ps, s)

def prepare(src, dst):
    with zipfile.ZipFile(src) as zi, zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zo:
        for it in zi.infolist():
            data = zi.read(it.filename)
            if it.filename.endswith('.xml'):
                s = data.decode('utf-8')
                for a, b in FONTS: s = s.replace(a, b)
                if re.match(r'xl/worksheets/sheet\d+\.xml$', it.filename): s = fix_sheet(s)
                data = s.encode('utf-8')
            zo.writestr(it, data)

def main():
    src, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    wb = openpyxl.load_workbook(src, read_only=False)
    sheets = []
    for ws in wb.worksheets:
        if ws.sheet_state != 'visible': continue
        title = ''
        for row in ws.iter_rows(min_row=1, max_row=6, values_only=True):
            for v in row:
                if isinstance(v, str) and '週' in v and '<' in v: title = v; break
            if title: break
        key = course_of(ws.title) or course_of(title)
        m = re.search(r'(\d{1,2})/(\d{1,2})週', title)
        sheets.append((ws.title, key, (int(m.group(1)), int(m.group(2))) if m else None))
    tmp = tempfile.mkdtemp()
    work = os.path.join(tmp, 'work.xlsx')
    prepare(src, work)
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', tmp, work],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
    pdf = os.path.join(tmp, 'work.pdf')
    pages = PdfReader(pdf).pages
    if len(pages) != len(sheets):
        sys.exit(f'ページ数({len(pages)})とシート数({len(sheets)})が一致しません。印刷範囲を確認してください')
    result = {}
    for i, (name, key, md) in enumerate(sheets, 1):
        if not key or not md:
            print(f'!! 判定できないシート: {name} key={key} week={md}', file=sys.stderr); continue
        start = monday(*md)
        if start.weekday() != 0: print(f'!! {name}: {start} は月曜ではありません', file=sys.stderr)
        fn = f'{start.isoformat()}_{key}.pdf'
        # qpdf で1ページだけ抜き出す（使わない画像を持ち込まないので軽い：約0.7MB/コース）
        subprocess.run(['qpdf', '--empty', '--pages', pdf, str(i), '--', '--object-streams=generate',
                        os.path.join(out, fn)], check=True)
        result.setdefault(start.isoformat(), {})[key] = 'pdf/' + fn
        print(f'{name} -> {fn}', file=sys.stderr)
    shutil.rmtree(tmp, ignore_errors=True)
    print(json.dumps([{'start': s, 'files': f} for s, f in sorted(result.items())], ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
