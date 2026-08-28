#!/usr/bin/env python3
"""Compose and validate a Starryear-Threefold-Memory artwork."""
import argparse, json
from pathlib import Path
from PIL import Image, ImageOps

RESAMPLE = Image.Resampling.LANCZOS

def fit(im, size, mode="cover", focus=(.5, .5)):
    im = ImageOps.exif_transpose(im).convert("RGB")
    if mode == "contain":
        placed = ImageOps.contain(im, size, RESAMPLE)
        canvas = Image.new("RGB", size, (243, 240, 232))
        canvas.paste(placed, ((size[0]-placed.width)//2, (size[1]-placed.height)//2))
        return canvas
    scale = max(size[0]/im.width, size[1]/im.height)
    im = im.resize((round(im.width*scale), round(im.height*scale)), RESAMPLE)
    left = round((im.width-size[0]) * focus[0])
    top = round((im.height-size[1]) * focus[1])
    return im.crop((left, top, left+size[0], top+size[1]))

def compose(top, photo, bottom, output, width=1920, panel_height=1080,
            mode="cover", focus_x=.5, focus_y=.5):
    if width <= 0 or panel_height <= 0 or not 0 <= focus_x <= 1 or not 0 <= focus_y <= 1:
        raise ValueError("invalid dimensions or focus")
    paths = [Path(top), Path(photo), Path(bottom)]
    if not all(p.is_file() for p in paths):
        raise FileNotFoundError("top, photo, and bottom must all exist")
    size = (width, panel_height)
    with Image.open(paths[0]) as im: a = fit(im, size)
    with Image.open(paths[1]) as im: b = fit(im, size, mode, (focus_x, focus_y))
    with Image.open(paths[2]) as im: c = fit(im, size)
    final = Image.new("RGB", (width, panel_height*3))
    for index, panel in enumerate((a, b, c)): final.paste(panel, (0, index*panel_height))
    output = Path(output); output.parent.mkdir(parents=True, exist_ok=True)
    if output.suffix.lower() in (".jpg", ".jpeg"):
        final.save(output, quality=95, subsampling=0, optimize=True)
    elif output.suffix.lower() == ".png": final.save(output, optimize=True)
    else: raise ValueError("output must be JPG or PNG")
    with Image.open(output) as check:
        assert check.size == (width, panel_height*3) and check.mode == "RGB"
    print(f"DELIVERY PASS: {output} ({width}x{panel_height*3}, RGB)")

def main():
    p = argparse.ArgumentParser()
    for name in ("top", "photo", "bottom", "output"): p.add_argument(f"--{name}")
    p.add_argument("--manifest", type=Path)
    p.add_argument("--width", type=int, default=1920)
    p.add_argument("--panel-height", type=int, default=1080)
    p.add_argument("--fit", choices=("cover", "contain"), default="cover")
    p.add_argument("--focus-x", type=float, default=.5); p.add_argument("--focus-y", type=float, default=.5)
    a = p.parse_args()
    if a.manifest:
        jobs = json.loads(a.manifest.read_text(encoding="utf-8")); jobs = jobs.get("jobs", jobs) if isinstance(jobs, dict) else jobs
        if not isinstance(jobs, list) or not jobs: p.error("manifest requires a non-empty jobs list")
        for job in jobs:
            if not all(k in job for k in ("top", "photo", "bottom", "output")): p.error("each job must explicitly map top, photo, bottom, output")
            compose(job["top"], job["photo"], job["bottom"], job["output"], int(job.get("width", a.width)), int(job.get("panel_height", a.panel_height)), job.get("fit", a.fit), float(job.get("focus_x", a.focus_x)), float(job.get("focus_y", a.focus_y)))
    elif all((a.top, a.photo, a.bottom, a.output)):
        compose(a.top, a.photo, a.bottom, a.output, a.width, a.panel_height, a.fit, a.focus_x, a.focus_y)
    else: p.error("provide --manifest or all four file arguments")

if __name__ == "__main__": main()
