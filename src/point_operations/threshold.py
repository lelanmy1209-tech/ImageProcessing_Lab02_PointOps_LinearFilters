import cv2


def threshold_image(image, threshold=128):
    """
    Chuyển ảnh sang ảnh nhị phân bằng phương pháp cắt ngưỡng.
    Cập nhật nhận vào numpy array thay vì đường dẫn.
    """
    if image is None:
        raise ValueError("Ảnh đầu vào không hợp lệ.")

    # Nếu là ảnh màu 3 kênh thì chuyển về ảnh xám trước khi cắt ngưỡng
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image

    _, result = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    return result