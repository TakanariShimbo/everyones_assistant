import cv2
import numpy as np


class ImageHandler:
    @staticmethod
    def read_image(image_path: str) -> np.ndarray:
        return cv2.imread(image_path)
