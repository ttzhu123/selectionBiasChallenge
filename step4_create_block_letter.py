"""
Step 4: Render a block letter on a white canvas for use as a selection-bias mask.
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFont


def create_block_letter_s(
    height: int,
    width: int,
    letter: str = "S",
    font_size_ratio: float = 0.9,
) -> np.ndarray:
    """
    Generate a block letter on a white background matching image dimensions.

    Parameters
    ----------
    height : int
        Image height in pixels.
    width : int
        Image width in pixels.
    letter : str
        Letter to render (default "S").
    font_size_ratio : float
        Font size as a fraction of min(height, width) (default 0.9).

    Returns
    -------
    np.ndarray
        Shape (height, width), float32 in [0, 1]: 0.0 = letter, 1.0 = background.
    """
    img = Image.new("L", (width, height), color=255)
    draw = ImageDraw.Draw(img)

    font_size = max(1, int(min(height, width) * font_size_ratio))
    font = None
    # (path, index) — index matters for .ttc collections (e.g. Helvetica on macOS)
    font_candidates = [
        ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 0),
        ("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 0),
        ("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 0),
        ("/Library/Fonts/Arial Bold.ttf", 0),
        ("/System/Library/Fonts/Helvetica.ttc", 0),
        ("/Windows/Fonts/arialbd.ttf", 0),
    ]
    for path, index in font_candidates:
        try:
            font = ImageFont.truetype(path, font_size, index=index)
            break
        except (OSError, IOError):
            continue

    if font is None:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), letter, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (width - text_w) // 2 - bbox[0]
    y = (height - text_h) // 2 - bbox[1]

    draw.text((x, y), letter, fill=0, font=font)

    return np.asarray(img, dtype=np.float32) / 255.0
