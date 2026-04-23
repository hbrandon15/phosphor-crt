import numpy as np
from PIL import Image

def load(path: str) -> np.ndarray: 
    img = Image.open(path).convert('RGB')
    return np.array(img, dtype=np.float32) / 255.0

def apply_subpixel_mask(img: np.ndarray) -> np.ndarray: 
    """
    Digitally re-creating each "pixel" (phosphor elements) -- one that glows red, green, and blue -- arranged as vertical stripes side by side. 
    Column 0: [1, 0, 0] — only red can pass through
    Column 1: [0, 1, 0] — only green can pass through
    Column 2: [0, 0, 1] — only blue can pass through
    Column 3: repeats red, and so on...
    """
    # img[y, x]  →  [R, G, B]   ← one pixel, three values
    h, w, _ = img.shape

    # create empty array of zeros the same size of provided image
    mask = np.zeros((h, w, 3), dtype=np.float32)

    # (step by 3 for each)
    # set first columns for only reds to pass 
    mask[:, 0::3, 0] = 1.0
    # set second columns for only green to pass
    mask[:, 1::3, 1] = 1.0
    # set the third columns for only blue to pass
    mask[:, 2::3, 2] = 1.0

    # return spatial filter
    return img * mask