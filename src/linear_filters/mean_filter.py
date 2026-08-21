import cv2


def mean_filter(image, kernel_size=5):
    """
    Bộ lọc trung bình (Mean / Average Filter) làm mịn ảnh.
    """
    if image is None:
        raise ValueError("Ảnh đầu vào không hợp lệ.")

    if isinstance(kernel_size, int):
        kernel_size = (kernel_size, kernel_size)

    return cv2.blur(image, kernel_size)