import sys
import numpy as np
from PIL import Image
from pipeline import load, apply_subpixel_mask


def main():

    img = load("assets/focal_white.png")
    result = apply_subpixel_mask(img)
    out = Image.fromarray((result * 255).astype(np.uint8))
    out.save("output/focal_white_subpixel.png")


if __name__ == "__main__":
    sys.exit(main())
