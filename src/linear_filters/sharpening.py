import cv2
import numpy as np


def sharpening(image):
    """
    Làm sắc nét ảnh bằng hàm tích chập cv2.filter2D (Siêu nhanh).
    """
    if image is None:
        raise ValueError("Ảnh đầu vào không hợp lệ.")

    # Kernel làm sắc nét 3x3
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ], dtype=np.float32)

    # Tích chập 2D siêu nhanh
    result = cv2.filter2D(image, -1, kernel)
    return result