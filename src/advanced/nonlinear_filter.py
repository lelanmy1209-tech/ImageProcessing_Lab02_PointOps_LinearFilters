import numpy as np


# ============================================================
# KIỂM TRA ẢNH
# ============================================================

def validate_image(image):
    """
    Kiểm tra ảnh đầu vào.

    Parameters:
        image: Ảnh dạng numpy array.

    Returns:
        None
    """

    if image is None:
        raise ValueError("Ảnh đầu vào không hợp lệ.")

    if image.ndim not in [2, 3]:
        raise ValueError(
            "Ảnh phải là grayscale hoặc ảnh màu."
        )


# ============================================================
# MEDIAN FILTER - GRAYSCALE
# ============================================================

def median_filter_gray(image, kernel_size=3):
    """
    Áp dụng Median Filter cho ảnh grayscale.

    Parameters:
        image: Ảnh grayscale.
        kernel_size: Kích thước kernel, phải là số lẻ.

    Returns:
        Ảnh sau khi lọc Median.
    """

    if kernel_size % 2 == 0:
        raise ValueError(
            "kernel_size phải là số lẻ."
        )

    if kernel_size < 3:
        raise ValueError(
            "kernel_size phải >= 3."
        )

    height, width = image.shape

    radius = kernel_size // 2

    # Padding ảnh
    padded_image = np.pad(
        image,
        (
            (radius, radius),
            (radius, radius)
        ),
        mode="edge"
    )

    # Ảnh kết quả
    result = np.zeros(
        (height, width),
        dtype=np.float64
    )

    # Duyệt từng pixel
    for i in range(height):
        for j in range(width):

            # Lấy vùng kernel
            region = padded_image[
                i:i + kernel_size,
                j:j + kernel_size
            ]

            # Median
            result[i, j] = np.median(
                region
            )

    return result


# ============================================================
# MEDIAN FILTER - ẢNH MÀU
# ============================================================

def median_filter_color(image, kernel_size=3):
    """
    Áp dụng Median Filter cho ảnh màu.

    Xử lý từng channel riêng biệt.

    Parameters:
        image: Ảnh màu.
        kernel_size: Kích thước kernel.

    Returns:
        Ảnh sau khi lọc.
    """

    height, width, channels = image.shape

    result = np.zeros(
        (height, width, channels),
        dtype=np.float64
    )

    for c in range(channels):

        result[:, :, c] = median_filter_gray(
            image[:, :, c],
            kernel_size
        )

    return result


# ============================================================
# MEDIAN FILTER
# ============================================================

def median_filter(image, kernel_size=3):
    """
    Áp dụng Median Filter.

    Parameters:
        image: Ảnh đầu vào.
        kernel_size: Kích thước kernel.

    Returns:
        Ảnh sau khi Median Filter.
    """

    validate_image(image)

    image_float = image.astype(
        np.float64
    )

    if image.ndim == 2:

        result = median_filter_gray(
            image_float,
            kernel_size
        )

    else:

        result = median_filter_color(
            image_float,
            kernel_size
        )

    result = np.clip(
        result,
        0,
        255
    )

    return result.astype(np.uint8)


# ============================================================
# BILATERAL FILTER - GRAYSCALE
# ============================================================

def bilateral_filter_gray(
    image,
    kernel_size=5,
    sigma_space=2.0,
    sigma_color=50.0
):
    """
    Áp dụng Bilateral Filter cho ảnh grayscale.

    Bilateral Filter sử dụng hai loại trọng số:

    1. Spatial Weight:
       Dựa trên khoảng cách không gian.

    2. Range Weight:
       Dựa trên sự khác biệt cường độ pixel.

    Parameters:
        image: Ảnh grayscale.
        kernel_size: Kích thước kernel.
        sigma_space: Độ lệch chuẩn không gian.
        sigma_color: Độ lệch chuẩn cường độ.

    Returns:
        Ảnh sau khi lọc Bilateral.
    """

    if kernel_size % 2 == 0:
        raise ValueError(
            "kernel_size phải là số lẻ."
        )

    if kernel_size < 3:
        raise ValueError(
            "kernel_size phải >= 3."
        )

    if sigma_space <= 0:
        raise ValueError(
            "sigma_space phải > 0."
        )

    if sigma_color <= 0:
        raise ValueError(
            "sigma_color phải > 0."
        )

    height, width = image.shape

    radius = kernel_size // 2

    # Padding
    padded_image = np.pad(
        image,
        (
            (radius, radius),
            (radius, radius)
        ),
        mode="edge"
    )

    # Tạo tọa độ kernel
    x = np.arange(
        -radius,
        radius + 1
    )

    X, Y = np.meshgrid(
        x,
        x
    )

    # Spatial Gaussian
    spatial_weight = np.exp(
        -(X ** 2 + Y ** 2)
        / (2 * sigma_space ** 2)
    )

    # Ảnh kết quả
    result = np.zeros(
        (height, width),
        dtype=np.float64
    )

    # Duyệt từng pixel
    for i in range(height):
        for j in range(width):

            # Pixel trung tâm
            center = padded_image[
                i + radius,
                j + radius
            ]

            # Vùng lân cận
            region = padded_image[
                i:i + kernel_size,
                j:j + kernel_size
            ]

            # ------------------------------------------------
            # Range Weight
            # ------------------------------------------------

            intensity_difference = (
                region - center
            )

            range_weight = np.exp(
                -(intensity_difference ** 2)
                / (2 * sigma_color ** 2)
            )

            # ------------------------------------------------
            # Tổng trọng số
            # ------------------------------------------------

            weights = (
                spatial_weight
                * range_weight
            )

            weight_sum = np.sum(
                weights
            )

            # Tránh chia cho 0
            if weight_sum == 0:
                result[i, j] = center

            else:
                result[i, j] = np.sum(
                    weights * region
                ) / weight_sum

    return result


# ============================================================
# BILATERAL FILTER - ẢNH MÀU
# ============================================================

def bilateral_filter_color(
    image,
    kernel_size=5,
    sigma_space=2.0,
    sigma_color=50.0
):
    """
    Áp dụng Bilateral Filter cho ảnh màu.

    Parameters:
        image: Ảnh màu.
        kernel_size: Kích thước kernel.
        sigma_space: Độ lệch chuẩn không gian.
        sigma_color: Độ lệch chuẩn màu.

    Returns:
        Ảnh sau khi lọc.
    """

    height, width, channels = image.shape

    result = np.zeros(
        (height, width, channels),
        dtype=np.float64
    )

    # Xử lý từng channel
    for c in range(channels):

        result[:, :, c] = bilateral_filter_gray(
            image[:, :, c],
            kernel_size,
            sigma_space,
            sigma_color
        )

    return result


# ============================================================
# BILATERAL FILTER
# ============================================================

def bilateral_filter(
    image,
    kernel_size=5,
    sigma_space=2.0,
    sigma_color=50.0
):
    """
    Áp dụng Bilateral Filter.

    Parameters:
        image: Ảnh đầu vào.
        kernel_size: Kích thước kernel.
        sigma_space: Độ lệch chuẩn không gian.
        sigma_color: Độ lệch chuẩn cường độ.

    Returns:
        Ảnh sau khi Bilateral Filter.
    """

    validate_image(image)

    image_float = image.astype(
        np.float64
    )

    if image.ndim == 2:

        result = bilateral_filter_gray(
            image_float,
            kernel_size,
            sigma_space,
            sigma_color
        )

    else:

        result = bilateral_filter_color(
            image_float,
            kernel_size,
            sigma_space,
            sigma_color
        )

    result = np.clip(
        result,
        0,
        255
    )

    return result.astype(np.uint8)


# ============================================================
# SO SÁNH MEDIAN VÀ BILATERAL
# ============================================================

def compare_nonlinear_filters(image):
    """
    Áp dụng cả Median và Bilateral Filter
    để so sánh kết quả.

    Parameters:
        image: Ảnh đầu vào.

    Returns:
        Dictionary chứa ảnh gốc,
        Median và Bilateral.
    """

    validate_image(image)

    median_result = median_filter(
        image,
        kernel_size=3
    )

    bilateral_result = bilateral_filter(
        image,
        kernel_size=5,
        sigma_space=2.0,
        sigma_color=50.0
    )

    return {
        "original": image,
        "median": median_result,
        "bilateral": bilateral_result
    }