import numpy as np
from PIL import Image

def load(path: str) -> np.ndarray: 
    img = Image.open(path).convert('RGB')
    return np.array(img, dtype=np.float32 / 255.0)