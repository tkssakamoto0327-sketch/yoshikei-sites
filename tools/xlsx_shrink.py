#!/usr/bin/env python3
"""献立表Excelの軽量化：EMF形式の盛付写真（ビットマップを包んだだけで1枚約0.9MB）を JPEG に置き換える。
Cloudflare Pages は1ファイル25MBまでなので、超える場合に使う。見た目（セル内の位置・大きさ）は変わらない。
usage: python3 -I tools/xlsx_shrink.py IN.xlsx OUT.xlsx
"""
import sys, re, io, struct, zipfile
from PIL import Image


def emf_to_image(d):
    o, best = 0, None
    while o + 8 <= len(d):
        t, s = struct.unpack_from('<II', d, o)
        if t == 81:   # EMR_STRETCHDIBITS
            ob, cb, off, cbits = struct.unpack_from('<IIII', d, o + 48)
            bmi, bits = d[o + ob:o + ob + cb], d[o + off:o + off + cbits]
            if not best or len(bits) > len(best[1]):
                best = (bmi, bits)
        if s == 0:
            break
        o += s
    if not best:
        raise ValueError('EMF にビットマップが見つからない')
    bmi, bits = best
    hdr = b'BM' + struct.pack('<IHHI', 14 + len(bmi) + len(bits), 0, 0, 14 + len(bmi))
    return Image.open(io.BytesIO(hdr + bmi + bits)).convert('RGB')


def main():
    src, dst = sys.argv[1:3]
    zi = zipfile.ZipFile(src)
    emfs = {i.filename: i for i in zi.infolist() if i.filename.startswith('xl/media/') and i.filename.lower().endswith('.emf')}
    new = {}
    for fn in emfs:
        im = emf_to_image(zi.read(fn))
        b = io.BytesIO()
        im.save(b, 'JPEG', quality=88, optimize=True)
        new[fn] = (fn[:-4] + '.jpeg', b.getvalue())
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zo:
        for i in zi.infolist():
            fn = i.filename
            if fn in new:
                zo.writestr(new[fn][0], new[fn][1], compress_type=zipfile.ZIP_STORED)
                continue
            if fn == 'docProps/thumbnail.emf':   # プレビュー画像（約1MB）は不要
                continue
            data = zi.read(fn)
            if fn.endswith('.rels'):
                t = data.decode('utf-8')
                for old, (nn, _) in new.items():
                    t = t.replace(old.split('/')[-1], nn.split('/')[-1])
                t = re.sub(r'<Relationship [^>]*thumbnail\.emf[^>]*/>', '', t)
                data = t.encode('utf-8')
            elif fn == '[Content_Types].xml':
                t = data.decode('utf-8')
                if 'Extension="jpeg"' not in t:
                    t = t.replace('<Default ', '<Default Extension="jpeg" ContentType="image/jpeg"/><Default ', 1)
                data = t.encode('utf-8')
            zo.writestr(fn, data)
    print(f'EMF {len(new)} 枚を JPEG に置き換え')


if __name__ == '__main__':
    main()
