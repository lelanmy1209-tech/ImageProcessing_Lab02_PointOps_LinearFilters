import numpy as np


def create_sharpening_kernel():
    """
    Tạo kernel làm sắc nét ảnh.

    Returns:
        numpy.ndarray: Sharpening kernel 3x3
    """

    kernel = np.array([
        [0, -1,  0],
        [-1, 5, -1],
        [0, -1,  0]
    ], dtype=np.float64)

    return kernel


def sharpening(image):
    """
    Làm sắc nét ảnh bằng phương pháp tích chập.

    Parameters:
        image: Ảnh đầu vào dạng numpy array.

    Returns:
        Ảnh sau khi làm sắc nét.
    """

    if image is None:
        raise ValueError("Ảnh đầu vào không hợp lệ.")

    # Tạo sharpening kernel
    kernel = create_sharpening_kernel()

    # Kernel 3x3 nên bán kính = 1
    kernel_size = 3
    radius = 1

    # Chuyển ảnh sang float để tính toán
    image_float = image.astype(np.float64)

    # ==================================================
    # ẢNH GRAYSCALE
    # ==================================================
    if image.ndim == 2:

        height, width = image.shape

        # Padding ảnh
        padded_image = np.pad(
            image_float,
            (
                (radius, radius),
                (radius, radius)
            ),
            mode="edge"
        )

        # Tạo ảnh kết quả
        result = np.zeros(
            (height, width),
            dtype=np.float64
        )

        # Duyệt từng pixel
        for i in range(height):
            for j in range(width):

                # Lấy vùng ảnh 3x3
                region = padded_image[
                    i:i + kernel_size,
                    j:j + kernel_size
                ]

                # Tích chập
                result[i, j] = np.sum(
                    region * kernel
                )

    # ==================================================
    # ẢNH MÀU
    # ==================================================
    elif image.ndim == 3:

        height, width, channels = image.shape

        # Padding ảnh
        padded_image = np.pad(
            image_float,
            (
                (radius, radius),
                (radius, radius),
                (0, 0)
            ),
            mode="edge"
        )

        # Tạo ảnh kết quả
        result = np.zeros(
            (height, width, channels),
            dtype=np.float64
        )

        # Duyệt từng pixel
        for i in range(height):
            for j in range(width):

                # Xử lý từng channel
                for c in range(channels):

                    # Lấy vùng 3x3
                    region = padded_image[
                        i:i + kernel_size,
                        j:j + kernel_size,
                        c
                    ]

                    # Tích chập
                    result[i, j, c] = np.sum(
                        region * kernel
                    )

    else:
        raise ValueError(
            "Ảnh phải là grayscale hoặc ảnh màu."
        )

    # Giới hạn giá trị pixel trong [0, 255]
    result = np.clip(result, 0, 255)

    # Chuyển về uint8
    result = result.astype(np.uint8)

    return result