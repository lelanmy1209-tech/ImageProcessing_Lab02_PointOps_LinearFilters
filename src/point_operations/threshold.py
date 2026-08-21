import cv2


def threshold_image(input_path, output_path, threshold=128):
    """
    Chuyển ảnh sang ảnh nhị phân bằng phương pháp cắt ngưỡng.

    Pixel >= threshold  -> 255
    Pixel < threshold   -> 0
    """

    # Đọc ảnh
    image = cv2.imread(input_path)

    if image is None:
        raise ValueError(f"Không thể đọc ảnh: {input_path}")

    # Chuyển sang ảnh xám
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Cắt ngưỡng
    _, result = cv2.threshold(
        gray,
        threshold,
        255,
        cv2.THRESH_BINARY
    )

    # Lưu ảnh
    cv2.imwrite(output_path, result)

    return result