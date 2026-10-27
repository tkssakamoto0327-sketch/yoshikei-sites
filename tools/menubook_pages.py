#!/usr/bin/env python3
"""ヨシケイ メニューブック用：PDF → 縦向き・傾き補正済みのページ画像（WebP）
usage:
  python3 menubook_pages.py KIND PDF OUTDIR PREFIX [--rotate ccw|cw|none]
KIND:
  portrait : 1ページ=縦1ページ（スマイル&テーブル）
  spreads  : 横長ページは中央で左右2ページに分割、縦長はそのまま（&more）
  lovyu    : ラビュ。1枚目は表紙＋一覧の折込→余白付きで2ページ化、2枚目以降は中央分割
  rotate   : 各ページを --rotate 方向に90°回して縦向きにし、白い余白を切り落とす（横倒しスキャンの特販）。回しても横長なら分割
出力: OUTDIR/PREFIX01.webp(1600x2264) と PREFIX01_s.webp(800x1132) …
"""
import sys, os, glob, subprocess, tempfile
import numpy as np, cv2
from PIL import Image

W, H = 1600, 2264

def render(pdf, dpi=200):
    d = tempfile.mkdtemp()
    subprocess.run(['pdftoppm', '-r', str(dpi), '-jpeg', '-jpegopt', 'quality=95', pdf, f'{d}/p'], check=True)
    return sorted(glob.glob(f'{d}/p-*.jpg'), key=lambda f: int(f.rsplit('-', 1)[1][:-4]))

def skew(g):
    s = 900 / g.shape[1]
    a = cv2.resize(g, None, fx=s, fy=s, interpolation=cv2.INTER_AREA)
    e = cv2.Canny(a, 60, 160).astype(np.float32); h, w = e.shape
    def sc(ang):
        M = cv2.getRotationMatrix2D((w / 2, h / 2), ang, 1)
        r = cv2.warpAffine(e, M, (w, h)); return np.var(r.sum(1)) + np.var(r.sum(0))
    b = max(np.arange(-1.5, 1.51, 0.1), key=sc)
    return float(max(np.arange(b - 0.1, b + 0.101, 0.025), key=sc))

def deskew(im):
    ang = skew(cv2.cvtColor(im, cv2.COLOR_BGR2GRAY))
    if abs(ang) >= 0.1:
        h, w = im.shape[:2]; M = cv2.getRotationMatrix2D((w / 2, h / 2), ang, 1)
        im = cv2.warpAffine(im, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        m = int(min(w, h) * np.sin(np.radians(abs(ang)))) + 3; im = im[m:h - m, m:w - m]
    return im, ang

def trim(im, th=225, frac=0.03, pad=4):
    """スキャナ台の余白（白）を切り落として紙の範囲だけにする"""
    g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY); m = (g < th).astype(np.float32)
    r = np.where(m.mean(1) > frac)[0]; c = np.where(m.mean(0) > frac)[0]
    if len(r) < 10 or len(c) < 10: return im
    y0, y1 = max(r[0] - pad, 0), min(r[-1] + pad, im.shape[0]); x0, x1 = max(c[0] - pad, 0), min(c[-1] + pad, im.shape[1])
    return im[y0:y1, x0:x1]

def letterbox(im):
    h, w = im.shape[:2]; s = min(W / w, H / h)
    r = cv2.resize(im, (int(w * s), int(h * s)), interpolation=cv2.INTER_AREA)
    c = np.full((H, W, 3), 255, np.uint8); y = (H - r.shape[0]) // 2; x = (W - r.shape[1]) // 2
    c[y:y + r.shape[0], x:x + r.shape[1]] = r; return c

def save(im, out, name, fit='stretch'):
    im = letterbox(im) if fit == 'letterbox' else cv2.resize(im, (W, H), interpolation=cv2.INTER_AREA)
    rgb = Image.fromarray(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
    rgb.save(f'{out}/{name}.webp', 'WEBP', quality=74, method=6)
    rgb.resize((800, 1132), Image.LANCZOS).save(f'{out}/{name}_s.webp', 'WEBP', quality=70, method=6)

def main():
    kind, pdf, out, prefix = sys.argv[1:5]
    rot = 'ccw'
    if '--rotate' in sys.argv: rot = sys.argv[sys.argv.index('--rotate') + 1]
    os.makedirs(out, exist_ok=True)
    n = 1
    def emit(im, fit='stretch'):
        nonlocal n
        im, a = deskew(im); save(im, out, f'{prefix}{n:02d}', fit)
        print(f'{prefix}{n:02d}  skew={a:+.2f}°  {im.shape[1]}x{im.shape[0]}'); n += 1
    for f in render(pdf, 300 if kind == 'lovyu' else 200):
        im = cv2.imread(f); h, w = im.shape[:2]
        if kind == 'portrait':
            emit(im)
        elif kind == 'rotate':
            code = {'ccw': cv2.ROTATE_90_COUNTERCLOCKWISE, 'cw': cv2.ROTATE_90_CLOCKWISE}.get(rot)
            if code is not None: im = cv2.rotate(im, code)
            im = trim(im)
            h, w = im.shape[:2]
            if w > h * 1.2:
                im, _ = deskew(im); W2 = im.shape[1] // 2; emit(im[:, :W2]); emit(im[:, W2:])
            else: emit(im)
        elif kind == 'spreads':
            if w > h * 1.2:
                im, _ = deskew(im); W2 = im.shape[1] // 2; emit(im[:, :W2]); emit(im[:, W2:])
            else: emit(im)
        elif kind == 'lovyu':
            if n == 1:
                g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY).astype(float)
                col = g[int(h * .08):int(h * .9)].mean(0)
                d = np.abs(np.diff(cv2.GaussianBlur(col.reshape(1, -1), (1, 9), 0)[0]))
                lo, hi = int(w * .6), int(w * .72); B = lo + int(np.argmax(d[lo:hi]))
                print('lovyu cover/index boundary x =', B, f'({B / w:.3f}W)')
                save(im[:, :B], out, f'{prefix}01', 'letterbox'); save(im[:, B + 6:], out, f'{prefix}02', 'letterbox')
                print(f'{prefix}01 cover, {prefix}02 index (letterboxed)'); n = 3
            else:
                im, _ = deskew(im); W2 = im.shape[1] // 2; emit(im[:, :W2]); emit(im[:, W2:])
        else:
            sys.exit('unknown KIND')
    print('pages:', n - 1)

if __name__ == '__main__':
    main()
