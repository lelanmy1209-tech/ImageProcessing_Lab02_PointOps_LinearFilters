import numpy as np


# ============================================================
# TẠO KERNEL SOBEL
# ============================================================

def create_sobel_kernels():
    """
    Tạo hai kernel Sobel theo hướng X và Y.

    Returns:
        sobel_x: Kernel phát hiện cạnh theo chiều dọc
        sobel_y: Kernel phát hiện cạnh theo chiều ngang
    """

    sobel_x = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ], dtype=np.float64)

    sobel_y = np.array([
        [-1, -2, -1],
        [0,  0,  0],
        [1,  2,  1]
    ], dtype=np.float64)

    return sobel_x, sobel_y


# ============================================================
# TẠO KERNEL PREWITT
# ============================================================

def create_prewitt_kernels():
    """
    Tạo hai kernel Prewitt theo hướng X và Y.

    Returns:
        prewitt_x: Kernel phát hiện cạnh theo chiều dọc
        prewitt_y: Kernel phát hiện cạnh theo chiều ngang
    """

    prewitt_x = np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ], dtype=np.float64)

    prewitt_y = np.array([
        [-1, -1, -1],
        [0,  0,  0],
        [1,  1,  1]
    ], dtype=np.float64)

    return prewitt_x, prewitt_y


# ============================================================
# CHUYỂN ẢNH SANG GRAYSCALE
# ============================================================

def to_grayscale(image):
    """
    Chuyển ảnh màu sang ảnh grayscale.

    Parameters:
        image: Ảnh đầu vào.

    Returns:
        Ảnh grayscale.
    """

    if image is None:
        raise ValueError("Ảnh đầu vào không hợp lệ.")

    # Nếu ảnh đã là grayscale
    if image.ndim == 2:
        return image.astype(np.float64)

    # Nếu ảnh là ảnh màu
    if image.ndim == 3:

        # Công thức chuyển grayscale
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
# CONVOLUTION
# ============================================================

def apply_kernel(image, kernel):
    """
    Áp dụng kernel lên ảnh bằng phép tích chập.

    Parameters:
        image: Ảnh grayscale.
        kernel: Kernel 3x3.

    Returns:
        Ảnh sau khi tích chập.
    """

    height, width = image.shape

    kernel_size = kernel.shape[0]
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

            # Lấy vùng ảnh tương ứng với kernel
            region = padded_image[
                i:i + kernel_size,
                j:j + kernel_size
            ]

            # Tích chập
            result[i, j] = np.sum(
                region * kernel
            )

    return result


# ============================================================
# TÍNH ĐỘ LỚN GRADIENT
# ============================================================

def calculate_gradient_magnitude(gradient_x, gradient_y):
    """
    Tính độ lớn gradient.

    G = sqrt(Gx^2 + Gy^2)

    Parameters:
        gradient_x: Gradient theo X.
        gradient_y: Gradient theo Y.

    Returns:
        Độ lớn gradient.
    """

    magnitude = np.sqrt(
        gradient_x ** 2
        + gradient_y ** 2
    )

    return magnitude


# ============================================================
# CHUẨN HÓA ẢNH
# ============================================================

def normalize_image(image):
    """
    Chuẩn hóa ảnh về khoảng [0, 255].

    Parameters:
        image: Ảnh đầu vào.

    Returns:
        Ảnh uint8 trong khoảng [0, 255].
    """

    min_value = np.min(image)
    max_value = np.max(image)

    # Tránh chia cho 0
    if max_value == min_value:
        return np.zeros(
            image.shape,
            dtype=np.uint8
        )

    normalized = (
        (image - min_value)
        / (max_value - min_value)
        * 255
    )

    normalized = np.clip(
        normalized,
        0,
        255
    )

    return normalized.astype(np.uint8)


# ============================================================
# SOBEL EDGE DETECTION
# ============================================================

def sobel_edge_detection(image):
    """
    Phát hiện cạnh bằng phương pháp Sobel.

    Parameters:
        image: Ảnh đầu vào.

    Returns:
        edge_image: Ảnh cạnh.
        gradient_x: Gradient theo X.
        gradient_y: Gradient theo Y.
    """

    # Chuyển sang grayscale
    gray = to_grayscale(image)

    # Lấy Sobel kernels
    sobel_x, sobel_y = create_sobel_kernels()

    # Tính gradient X
    gradient_x = apply_kernel(
        gray,
        sobel_x
    )

    # Tính gradient Y
    gradient_y = apply_kernel(
        gray,
        sobel_y
    )

    # Tính độ lớn gradient
    magnitude = calculate_gradient_magnitude(
        gradient_x,
        gradient_y
    )

    # Chuẩn hóa
    edge_image = normalize_image(
        magnitude
    )

    return edge_image, gradient_x, gradient_y


# ============================================================
# PREWITT EDGE DETECTION
# ============================================================

def prewitt_edge_detection(image):
    """
    Phát hiện cạnh bằng phương pháp Prewitt.

    Parameters:
        image: Ảnh đầu vào.

    Returns:
        edge_image: Ảnh cạnh.
        gradient_x: Gradient theo X.
        gradient_y: Gradient theo Y.
    """

    # Chuyển sang grayscale
    gray = to_grayscale(image)

    # Lấy Prewitt kernels
    prewitt_x, prewitt_y = create_prewitt_kernels()

    # Tính gradient X
    gradient_x = apply_kernel(
        gray,
        prewitt_x
    )

    # Tính gradient Y
    gradient_y = apply_kernel(
        gray,
        prewitt_y
    )

    # Tính độ lớn gradient
    magnitude = calculate_gradient_magnitude(
        gradient_x,
        gradient_y
    )

    # Chuẩn hóa
    edge_image = normalize_image(
        magnitude
    )

    return edge_image, gradient_x, gradient_y


# ============================================================
# HÀM TỔNG HỢP
# ============================================================

def edge_detection(image, method="sobel"):
    """
    Phát hiện cạnh bằng Sobel hoặc Prewitt.

    Parameters:
        image: Ảnh đầu vào.
        method: "sobel" hoặc "prewitt".

    Returns:
        Ảnh phát hiện cạnh.
    """

    method = method.lower()

    if method == "sobel":

        edge_image, _, _ = sobel_edge_detection(
            image
        )

    elif method == "prewitt":

        edge_image, _, _ = prewitt_edge_detection(
            image
        )

    else:
        raise ValueError(
            "method phải là 'sobel' hoặc 'prewitt'."
        )

    return edge_image