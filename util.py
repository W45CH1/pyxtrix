from PIL import Image
from numpy import asarray


def load_image(path: str):
    return asarray(Image.open(path))
