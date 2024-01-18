import cv2
import numpy as np


class ImageHandler:
    @staticmethod
    def read_image_depth32(image_path: str) -> np.ndarray:
        image_bgra = cv2.imread(image_path, flags=cv2.IMREAD_UNCHANGED)
        image_rgba = cv2.cvtColor(src=image_bgra, code=cv2.COLOR_BGRA2RGBA)
        return image_rgba