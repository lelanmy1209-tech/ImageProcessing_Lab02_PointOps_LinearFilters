import cv2


def change_brightness(image, beta=50):
    """
    Thay đổi độ sáng của ảnh.
    beta > 0: Tăng sáng
    beta < 0: Giảm sáng
    """
    if image is None:
        raise ValueError("Ảnh đầu vào không hợp lệ.")

    return cv2.convertScaleAbs(image, alpha=1.0, beta=beta)