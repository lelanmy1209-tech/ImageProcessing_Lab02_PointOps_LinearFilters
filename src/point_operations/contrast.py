import cv2


def change_contrast(image, alpha=1.5):
    """
    Thay đổi độ tương phản của ảnh.
    alpha > 1.0: Tăng tương phản
    0 < alpha < 1.0: Giảm tương phản
    """
    if image is None:
        raise ValueError("Ảnh đầu vào không hợp lệ.")

    return cv2.convertScaleAbs(image, alpha=alpha, beta=0)