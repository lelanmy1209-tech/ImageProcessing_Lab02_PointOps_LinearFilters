import sys
from pathlib import Path

# Thêm thư mục gốc dự án vào sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

# Import module IO hỗ trợ đường dẫn tiếng Việt
from src.io.image_io import read_image, save_image

# 1. Point Operations
from src.point_operations.negative import negative_image
from src.point_operations.brightness import change_brightness
from src.point_operations.contrast import change_contrast
from src.point_operations.threshold import threshold_image

# 2. Linear Filters
from src.linear_filters.gaussian_filter import gaussian_filter
from src.linear_filters.mean_filter import mean_filter
from src.linear_filters.sharpening import sharpening as sharpen_image


def main():
    # Khai báo đường dẫn đầu vào và đầu ra
    input_path = ROOT_DIR / "data" / "input" / "text.jpg"
    output_dir = ROOT_DIR / "data" / "output"

    # Đọc ảnh gốc
    img = read_image(input_path)
    print("--- Đang xử lý các thuật toán ---")

    # 1. Point Operations
    save_image(negative_image(img), output_dir / "negative.jpg")
    save_image(change_brightness(img, beta=50), output_dir / "brightness_plus.jpg")
    save_image(change_contrast(img, alpha=1.5), output_dir / "contrast_high.jpg")
    save_image(threshold_image(img, threshold=128), output_dir / "threshold.jpg")

    # 2. Linear Filters
    save_image(gaussian_filter(img, kernel_size=5, sigma=1.0), output_dir / "gaussian_blur.jpg")
    save_image(mean_filter(img, kernel_size=5), output_dir / "mean_blur.jpg")
    save_image(sharpen_image(img), output_dir / "sharpen.jpg")

    print("\nHoàn thành 100%! Hãy kiểm tra thư mục data/output/.")


if __name__ == "__main__":
    main()