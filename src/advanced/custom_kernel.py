import numpy as np


# ============================================================
# KIỂM TRA KERNEL
# ============================================================

def validate_kernel(kernel):
    """
    Kiểm tra kernel có hợp lệ hay không.

    Parameters:
        kernel: Ma trận kernel.

    Returns:
        kernel: Kernel dạng numpy array.
    """

    kernel = np.asarray(kernel, dtype=np.float64)

    # Kernel phải là ma trận 2 chiều
    if kernel.ndim != 2:
        raise ValueError(
            "Kernel phải là ma trận 2 chiều."
        )

    rows, cols = kernel.shape

    # Kernel phải có kích thước lẻ
    if rows % 2 == 0 or cols % 2 == 0:
        raise ValueError(
            "Kích thước kernel phải là số lẻ."
        )

    return kernel


# ============================================================
# TẠO CUSTOM KERNEL
# ============================================================

def create_custom_kernel(kernel):
    """
    Tạo kernel tùy chỉnh từ ma trận do người dùng cung cấp.

    Parameters:
        kernel: Ma trận kernel.

    Returns:
        Kernel đã được kiểm tra.
    """

    return validate_kernel(kernel)


# ============================================================
# CHUYỂN ẢNH SANG GRAYSCALE
# ============================================================

def to_grayscale(image):
    """
    Chuyển ảnh màu sang ảnh grayscale.

    Parameters:
        image: Ảnh đầu vào.

    Returns:
        Ảnh grayscale dạng float64.
    """

    if image is None:
        raise ValueError(
            "Ảnh đầu vào không hợp lệ."
        )

    # Nếu ảnh đã là grayscale
    if image.ndim == 2:
        return image.astype(np.float64)

    # Nếu ảnh màu
    if image.ndim == 3:

        gray = (
            0.299 * image[:, :, 0]
            + 0.587 * image[:, :, 1]
            + 0.114 * image[:, :, 2]
        )

        return gray.astype(np.float64)

    raise ValueError(
        "Ảnh phải là grayscale hoặc ảnh màu."
    )


# ============================================================
# ÁP DỤNG KERNEL CHO ẢNH GRAYSCALE
# ============================================================

def apply_kernel_gray(image, kernel):
    """
    Áp dụng custom kernel lên ảnh grayscale.

    Parameters:
        image: Ảnh grayscale.
        kernel: Kernel xử lý ảnh.

    Returns:
        Ảnh sau khi convolution.
    """

    height, width = image.shape

    kernel_height, kernel_width = kernel.shape

    radius_y = kernel_height // 2
    radius_x = kernel_width // 2

    # Padding ảnh
    padded_image = np.pad(
        image,
        (
            (radius_y, radius_y),
            (radius_x, radius_x)
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

            # Lấy vùng ảnh tương ứng với kernel
            region = padded_image[
                i:i + kernel_height,
                j:j + kernel_width
            ]

            # Convolution
            result[i, j] = np.sum(
                region * kernel
            )

    return result


# ============================================================
# ÁP DỤNG KERNEL CHO ẢNH MÀU
# ============================================================

def apply_kernel_color(image, kernel):
    """
    Áp dụng custom kernel cho từng channel của ảnh màu.

    Parameters:
        image: Ảnh màu.
        kernel: Kernel xử lý ảnh.

    Returns:
        Ảnh sau khi convolution.
    """

    height, width, channels = image.shape

    result = np.zeros(
        (height, width, channels),
        dtype=np.float64
    )

    # Xử lý từng channel
    for c in range(channels):

        result[:, :, c] = apply_kernel_gray(
            image[:, :, c],
            kernel
        )

    return result


# ============================================================
# HÀM ÁP DỤNG CUSTOM KERNEL
# ============================================================

def apply_custom_kernel(image, kernel):
    """
    Áp dụng kernel tùy chỉnh lên ảnh.

    Parameters:
        image: Ảnh đầu vào.
        kernel: Kernel tùy chỉnh.

    Returns:
        Ảnh sau khi xử lý.
    """

    if image is None:
        raise ValueError(
            "Ảnh đầu vào không hợp lệ."
        )

    # Kiểm tra kernel
    kernel = validate_kernel(kernel)

    # Chuyển ảnh sang float
    image_float = image.astype(np.float64)

    # --------------------------------------------------------
    # ẢNH GRAYSCALE
    # --------------------------------------------------------

    if image.ndim == 2:

        result = apply_kernel_gray(
            image_float,
            kernel
        )

    # --------------------------------------------------------
    # ẢNH MÀU
    # --------------------------------------------------------

    elif image.ndim == 3:

        result = apply_kernel_color(
            image_float,
            kernel
        )

    else:

        raise ValueError(
            "Ảnh phải là grayscale hoặc ảnh màu."
        )

    # Giới hạn giá trị pixel
    result = np.clip(
        result,
        0,
        255
    )

    # Chuyển sang uint8
    result = result.astype(np.uint8)

    return result


# ============================================================
# MỘT SỐ KERNEL MẪU
# ============================================================

def blur_kernel():
    """
    Kernel làm mờ 3x3.
    """

    return np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ], dtype=np.float64) / 9


def sharpen_kernel():
    """
    Kernel làm sắc nét.
    """

    return np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ], dtype=np.float64)


def edge_kernel():
    """
    Kernel phát hiện cạnh.
    """

    return np.array([
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]
    ], dtype=np.float64)


# ============================================================
# HÀM CHẠY CUSTOM KERNEL
# ============================================================

def custom_kernel_filter(
    image,
    kernel_type="sharpen"
):
    """
    Áp dụng một kernel mẫu.

    Parameters:
        image: Ảnh đầu vào.
        kernel_type:
            - "blur"
            - "sharpen"
            - "edge"

    Returns:
        Ảnh sau khi xử lý.
    """

    kernel_type = kernel_type.lower()

    if kernel_type == "blur":

        kernel = blur_kernel()

    elif kernel_type == "sharpen":

        kernel = sharpen_kernel()

    elif kernel_type == "edge":

        kernel = edge_kernel()

    else:

        raise ValueError(
            "kernel_type phải là "
            "'blur', 'sharpen' hoặc 'edge'."
        )

    return apply_custom_kernel(
        image,
        kernel
    )