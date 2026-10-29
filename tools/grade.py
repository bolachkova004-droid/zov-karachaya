"""Единая цветокоррекция «Зов Карачая»: небо → сланец, зелень → олива,
тени → тёплый уголь (#1c1c1a), света → бумага (#f3efe6)."""
import sys, numpy as np
from PIL import Image, ImageOps

def smooth(x, a, b):  # 0 at a, 1 at b
    t = np.clip((x - a) / (b - a), 0, 1); return t * t * (3 - 2 * t)

def band(h, lo, hi, soft):  # hue window (degrees) with soft edges
    return smooth(h, lo - soft, lo) * (1 - smooth(h, hi, hi + soft))

def grade(im):
    hsv = np.asarray(im.convert('HSV')).astype(np.float32) / 255.0
    h, s, v = hsv[..., 0] * 360, hsv[..., 1], hsv[..., 2]
    sat_w = smooth(s, .08, .3)
    blue = band(h, 175, 250, 25) * sat_w
    green = band(h, 65, 165, 20) * sat_w
    # небо: в приглушённый сланцево-голубой, чуть темнее
    h = h + (205 - h) * .35 * blue
    s = s * (1 - .62 * blue)
    v = v * (1 - .06 * blue)
    # зелень: к оливе
    h = h + (62 - h) * .4 * green
    s = s * (1 - .25 * green)
    s = s * .9
    hsv2 = np.stack([(h % 360) / 360, np.clip(s, 0, 1), np.clip(v, 0, 1)], -1)
    rgb = np.asarray(Image.fromarray((hsv2 * 255).astype(np.uint8), 'HSV').convert('RGB')).astype(np.float32) / 255
    # мягкая S-кривая
    rgb = rgb + .2 * (rgb - .5) * (1 - np.abs(2 * rgb - 1))
    # тональный диапазон: уголь → бумага
    lo = np.array([22, 21, 19]) / 255; hi = np.array([243, 239, 230]) / 255
    rgb = lo + rgb * (hi - lo)
    # тёплые полутона
    l = rgb.mean(-1, keepdims=True); mid = 4 * l * (1 - l)
    rgb = rgb + mid * np.array([.022, .006, -.022])
    return Image.fromarray((np.clip(rgb, 0, 1) * 255 + .5).astype(np.uint8))

if __name__ == '__main__':
    src, dst, w = sys.argv[1], sys.argv[2], int(sys.argv[3])
    rot = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    if rot: im = im.rotate(rot, expand=True)
    if im.width > w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    grade(im).save(dst, quality=82, optimize=True, progressive=True)
    print(dst, im.size)
