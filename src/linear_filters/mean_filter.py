import cv2


def mean_filter(input_path, output_path, kernel_size=3):
    """
    Lọc trung bình (Mean Filter).

    kernel_size: kích thước kernel, ví dụ 3, 5, 7.
    """

    # Đọc ảnh
    image = cv2.imread(input_path)

    if image is None:
        raise ValueError(f"Không thể đọc ảnh: {input_path}")

    # Áp dụng Mean Filter
    result = cv2.blur(
        image,
        (kernel_size, kernel_size)
    )

    # Lưu ảnh
    cv2.imwrite(output_path, result)

    return result