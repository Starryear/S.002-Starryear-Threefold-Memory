#!/usr/bin/env python3
"""Assemble upper abstraction, source evidence, and lower abstraction without forcing orientation."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps


def normalized_pair(value: str) -> tuple[float, float]:
    try:
        x_text, y_text = value.split(",", 1)
        pair = (float(x_text), float(y_text))
    except (ValueError, TypeError) as exc:
        raise argparse.ArgumentTypeError("position must be x,y between 0 and 1") from exc
    if any(component < 0 or component > 1 for component in pair):
        raise argparse.ArgumentTypeError("position components must be between 0 and 1")
    return pair


def ratio_value(value: str) -> str | tuple[float, float]:
    if value == "source":
        return value
    try:
        width_text, height_text = value.split(":", 1)
        ratio = (float(width_text), float(height_text))
    except (ValueError, TypeError) as exc:
        raise argparse.ArgumentTypeError("panel ratio must be 'source' or W:H") from exc
    if ratio[0] <= 0 or ratio[1] <= 0:
        raise argparse.ArgumentTypeError("panel ratio values must be positive")
    return ratio


def open_oriented(path: Path) -> Image.Image:
    with Image.open(path) as image:
        return ImageOps.exif_transpose(image).convert("RGB")


def cover(image: Image.Image, size: tuple[int, int], centering: tuple[float, float]) -> Image.Image:
    return ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=centering)


def contain(image: Image.Image, size: tuple[int, int], background: str) -> Image.Image:
    return ImageOps.pad(
        image,
        size,
        method=Image.Resampling.LANCZOS,
        color=background,
        centering=(0.5, 0.5),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--top", required=True, type=Path)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--bottom", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--width", type=int, default=1200)
    parser.add_argument("--panel-ratio", type=ratio_value, default="source")
    parser.add_argument("--source-fit", choices=("contain", "cover"), default="contain")
    parser.add_argument("--background", default="#111111")
    parser.add_argument("--top-position", type=normalized_pair, default=(0.5, 0.5))
    parser.add_argument("--source-position", type=normalized_pair, default=(0.5, 0.5))
    parser.add_argument("--bottom-position", type=normalized_pair, default=(0.5, 0.5))
    parser.add_argument("--brightness", type=float, default=1.0)
    parser.add_argument("--contrast", type=float, default=1.0)
    args = parser.parse_args()

    if args.width < 300:
        parser.error("--width must be at least 300")
    if not 0.9 <= args.brightness <= 1.1:
        parser.error("--brightness must stay between 0.9 and 1.1")
    if not 0.9 <= args.contrast <= 1.1:
        parser.error("--contrast must stay between 0.9 and 1.1")
    for path in (args.top, args.source, args.bottom):
        if not path.is_file():
            parser.error(f"input file does not exist: {path}")
    return args


def main() -> None:
    args = parse_args()
    top_image = open_oriented(args.top)
    source_image = open_oriented(args.source)
    bottom_image = open_oriented(args.bottom)

    if args.panel_ratio == "source":
        panel_height = round(args.width * source_image.height / source_image.width)
    else:
        ratio_width, ratio_height = args.panel_ratio
        panel_height = round(args.width * ratio_height / ratio_width)
    panel_size = (args.width, panel_height)

    top = cover(top_image, panel_size, args.top_position)
    bottom = cover(bottom_image, panel_size, args.bottom_position)
    if args.source_fit == "cover":
        source = cover(source_image, panel_size, args.source_position)
    else:
        source = contain(source_image, panel_size, args.background)

    source = ImageEnhance.Brightness(source).enhance(args.brightness)
    source = ImageEnhance.Contrast(source).enhance(args.contrast)

    canvas = Image.new("RGB", (args.width, panel_height * 3), args.background)
    canvas.paste(top, (0, 0))
    canvas.paste(source, (0, panel_height))
    canvas.paste(bottom, (0, panel_height * 2))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.suffix.lower() in {".jpg", ".jpeg"}:
        canvas.save(args.output, quality=95, subsampling=0)
    else:
        canvas.save(args.output)


if __name__ == "__main__":
    main()
