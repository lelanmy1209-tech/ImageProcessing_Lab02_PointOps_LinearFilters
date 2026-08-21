import numpy as np


def negative_image(image):
    """
    Tạo ảnh âm bản (Negative Image) từ mảng numpy array.
    Công thức: s = L - 1 - r (với L = 256)
    """
    if image is None:
        raise ValueError("Ảnh đầu vào không hợp lệ.")

    return 255 - image