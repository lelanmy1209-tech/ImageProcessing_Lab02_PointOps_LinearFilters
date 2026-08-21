import os

from point_operations.brightness import change_brightness
from point_operations.contrast import change_contrast
from point_operations.negative import negative_image
from point_operations.threshold import threshold_image

from linear_filters.mean_filter import mean_filter
from linear_filters.gaussian_filter import gaussian_filter
from linear_filters.sharpening import sharpen_image


def main():
    # =========================
    # 1. Đường dẫn ảnh đầu vào
    # =========================
    input_path = "data/input/input.jpg"

    # Thư mục lưu kết quả
    output_point = "data/output/point_operations"
    output_linear = "data/output/linear_filters"

    os.makedirs(output_point, exist_ok=True)
    os.makedirs(output_linear, exist_ok=True)

    # =========================
    # 2. Point Operations
    # =========================

    # Thay đổi độ sáng
    change_brightness(
        input_path,
        os.path.join(output_point, "brightness.jpg"),
        beta=50
    )

    # Thay đổi độ tương phản
    change_contrast(
        input_path,
        os.path.join(output_point, "contrast.jpg"),
        alpha=1.5
    )

    # Biến đổi âm bản
    negative_image(
        input_path,
        os.path.join(output_point, "negative.jpg")
    )

    # Cắt ngưỡng
    threshold_image(
        input_path,
        os.path.join(output_point, "threshold.jpg"),
        threshold=128
    )

    # =========================
    # 3. Linear Filters
    # =========================

    # Mean Filter
    mean_filter(
        input_path,
        os.path.join(output_linear, "mean.jpg"),
        kernel_size=3
    )

    # Gaussian Filter
    gaussian_filter(
        input_path,
        os.path.join(output_linear, "gaussian.jpg"),
        kernel_size=5,
        sigma=1.0
    )

    # Sharpening
    sharpen_image(
        input_path,
        os.path.join(output_linear, "sharpening.jpg")
    )

    print("====================================")
    print("XỬ LÝ ẢNH HOÀN TẤT")
    print("====================================")
    print("Kết quả Point Operations:")
    print(output_point)
    print()
    print("Kết quả Linear Filters:")
    print(output_linear)


if __name__ == "__main__":
    main()