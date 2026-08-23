import numpy as np

from src.linear_filters.mean_filter import mean_filter
from src.linear_filters.gaussian_filter import gaussian_filter
from src.linear_filters.sharpening import sharpening

from src.advanced.edge_detection import (
    sobel_edge_detection,
    prewitt_edge_detection
)


# ============================================================
# CHẠY CÁC BỘ LỌC
# ============================================================

def apply_all_filters(image):
    """
    Áp dụng nhiều bộ lọc lên cùng một ảnh.

    Parameters:
        image: Ảnh đầu vào.

    Returns:
        Dictionary chứa kết quả của từng bộ lọc.
    """

    if image is None:
        raise ValueError(
            "Ảnh đầu vào không hợp lệ."
        )

    results = {}

    # --------------------------------------------------------
    # MEAN FILTER
    # --------------------------------------------------------

    results["mean"] = mean_filter(
        image,
        kernel_size=3
    )

    # --------------------------------------------------------
    # GAUSSIAN FILTER
    # --------------------------------------------------------

    results["gaussian"] = gaussian_filter(
        image,
        kernel_size=5,
        sigma=1.0
    )

    # --------------------------------------------------------
    # SHARPENING
    # --------------------------------------------------------

    results["sharpening"] = sharpening(
        image
    )

    # --------------------------------------------------------
    # SOBEL
    # --------------------------------------------------------

    sobel_result, sobel_x, sobel_y = (
        sobel_edge_detection(image)
    )

    results["sobel"] = sobel_result
    results["sobel_x"] = sobel_x
    results["sobel_y"] = sobel_y

    # --------------------------------------------------------
    # PREWITT
    # --------------------------------------------------------

    prewitt_result, prewitt_x, prewitt_y = (
        prewitt_edge_detection(image)
    )

    results["prewitt"] = prewitt_result
    results["prewitt_x"] = prewitt_x
    results["prewitt_y"] = prewitt_y

    return results


# ============================================================
# SO SÁNH CÁC BỘ LỌC LÀM MỜ
# ============================================================

def compare_blur_filters(image):
    """
    So sánh Mean Filter và Gaussian Filter.

    Parameters:
        image: Ảnh đầu vào.

    Returns:
        Dictionary chứa kết quả Mean và Gaussian.
    """

    if image is None:
        raise ValueError(
            "Ảnh đầu vào không hợp lệ."
        )

    results = {
        "original": image,

        "mean": mean_filter(
            image,
            kernel_size=3
        ),

        "gaussian": gaussian_filter(
            image,
            kernel_size=5,
            sigma=1.0
        )
    }

    return results


# ============================================================
# SO SÁNH CÁC BỘ LỌC PHÁT HIỆN CẠNH
# ============================================================

def compare_edge_filters(image):
    """
    So sánh Sobel và Prewitt.

    Parameters:
        image: Ảnh đầu vào.

    Returns:
        Dictionary chứa kết quả Sobel và Prewitt.
    """

    if image is None:
        raise ValueError(
            "Ảnh đầu vào không hợp lệ."
        )

    sobel_result, _, _ = (
        sobel_edge_detection(image)
    )

    prewitt_result, _, _ = (
        prewitt_edge_detection(image)
    )

    results = {
        "original": image,
        "sobel": sobel_result,
        "prewitt": prewitt_result
    }

    return results


# ============================================================
# TÍNH ĐỘ SÁNG TRUNG BÌNH
# ============================================================

def calculate_mean_intensity(image):
    """
    Tính cường độ pixel trung bình của ảnh.

    Parameters:
        image: Ảnh đầu vào.

    Returns:
        Giá trị cường độ trung bình.
    """

    if image is None:
        raise ValueError(
            "Ảnh đầu vào không hợp lệ."
        )

    return float(
        np.mean(image)
    )


# ============================================================
# TÍNH ĐỘ LỆCH CHUẨN
# ============================================================

def calculate_std(image):
    """
    Tính độ lệch chuẩn của ảnh.

    Độ lệch chuẩn càng lớn,
    mức độ biến thiên cường độ pixel càng cao.

    Parameters:
        image: Ảnh đầu vào.

    Returns:
        Độ lệch chuẩn.
    """

    if image is None:
        raise ValueError(
            "Ảnh đầu vào không hợp lệ."
        )

    return float(
        np.std(image)
    )


# ============================================================
# TẠO BẢNG SO SÁNH
# ============================================================

def generate_comparison_metrics(
    original,
    results
):
    """
    Tạo các chỉ số để so sánh kết quả.

    Parameters:
        original: Ảnh gốc.
        results: Dictionary kết quả các bộ lọc.

    Returns:
        Dictionary chứa các metrics.
    """

    if original is None:
        raise ValueError(
            "Ảnh gốc không hợp lệ."
        )

    metrics = {}

    # Metrics của ảnh gốc
    metrics["original"] = {
        "mean": calculate_mean_intensity(
            original
        ),
        "std": calculate_std(
            original
        )
    }

    # Metrics của từng kết quả
    for name, image in results.items():

        # Bỏ qua gradient X/Y
        if name.endswith("_x"):
            continue

        if name.endswith("_y"):
            continue

        if image is None:
            continue

        metrics[name] = {
            "mean": calculate_mean_intensity(
                image
            ),
            "std": calculate_std(
                image
            )
        }

    return metrics


# ============================================================
# IN KẾT QUẢ SO SÁNH
# ============================================================

def print_comparison(metrics):
    """
    In bảng so sánh các bộ lọc.

    Parameters:
        metrics: Dictionary metrics.
    """

    print("\n")
    print("=" * 65)
    print("SO SÁNH KẾT QUẢ CÁC BỘ LỌC")
    print("=" * 65)

    print(
        f"{'Filter':<20}"
        f"{'Mean':>15}"
        f"{'Std':>15}"
    )

    print("-" * 65)

    for name, values in metrics.items():

        print(
            f"{name:<20}"
            f"{values['mean']:>15.2f}"
            f"{values['std']:>15.2f}"
        )

    print("=" * 65)


# ============================================================
# HÀM SO SÁNH TỔNG QUÁT
# ============================================================

def compare_filters(image):
    """
    Chạy toàn bộ quá trình so sánh bộ lọc.

    Parameters:
        image: Ảnh đầu vào.

    Returns:
        results: Kết quả của các bộ lọc.
        metrics: Các chỉ số so sánh.
    """

    if image is None:
        raise ValueError(
            "Ảnh đầu vào không hợp lệ."
        )

    # Chạy tất cả bộ lọc
    results = apply_all_filters(
        image
    )

    # Tính metrics
    metrics = generate_comparison_metrics(
        image,
        results
    )

    # In kết quả
    print_comparison(
        metrics
    )

    return results, metrics
