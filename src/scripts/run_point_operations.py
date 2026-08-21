"""
run_linear_filters.py

Chạy toàn bộ các bộ lọc tuyến tính:
1. Mean Filter
2. Gaussian Filter
3. Sharpening

Kết quả được lưu vào:
data/output/linear_filters/
"""

import sys
from pathlib import Path


# ============================================================
# 1. XÁC ĐỊNH THƯ MỤC GỐC PROJECT
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Cho phép import module từ thư mục gốc project
sys.path.insert(0, str(PROJECT_ROOT))


# ============================================================
# 2. IMPORT MODULE
# ============================================================

from src.io.image_io import read_image, save_image

from src.linear_filters.mean_filter import mean_filter
from src.linear_filters.gaussian_filter import gaussian_filter
from src.linear_filters.sharpening import sharpening


# ============================================================
# 3. CẤU HÌNH ĐƯỜNG DẪN
# ============================================================

INPUT_DIR = PROJECT_ROOT / "data" / "input"

OUTPUT_DIR = PROJECT_ROOT / "data" / "output" / "linear_filters"

# Tự động tạo thư mục output nếu chưa tồn tại
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# 4. TÌM ẢNH ĐẦU VÀO
# ============================================================

def find_input_image():
    """
    Tìm ảnh đầu tiên trong thư mục data/input.

    Hỗ trợ:
    - JPG
    - JPEG
    - PNG
    - BMP
    """

    supported_formats = [
        ".jpg",
        ".jpeg",
        ".png",
        ".bmp"
    ]

    for file in INPUT_DIR.iterdir():

        if (
            file.is_file()
            and file.suffix.lower() in supported_formats
        ):
            return file

    return None


# ============================================================
# 5. CHƯƠNG TRÌNH CHÍNH
# ============================================================

def main():

    print("=" * 60)
    print("       LINEAR FILTERS - IMAGE PROCESSING LAB 02")
    print("=" * 60)

    # --------------------------------------------------------
    # Kiểm tra thư mục input
    # --------------------------------------------------------

    if not INPUT_DIR.exists():

        print(f"[ERROR] Không tìm thấy thư mục:")
        print(INPUT_DIR)

        return

    # --------------------------------------------------------
    # Tìm ảnh đầu vào
    # --------------------------------------------------------

    input_file = find_input_image()

    if input_file is None:

        print("[ERROR] Không tìm thấy ảnh trong:")
        print(INPUT_DIR)

        print("\nVui lòng thêm ảnh .jpg, .jpeg, .png hoặc .bmp")

        return

    print(f"\n[INPUT] {input_file.name}")

    # --------------------------------------------------------
    # Đọc ảnh
    # --------------------------------------------------------

    image = read_image(str(input_file))

    if image is None:

        print("[ERROR] Không thể đọc ảnh.")

        return

    print("[OK] Đọc ảnh thành công.")


    # ========================================================
    # 1. MEAN FILTER
    # ========================================================

    print("\n[1/3] Đang chạy Mean Filter...")

    try:

        mean_result = mean_filter(
            image,
            kernel_size=3
        )

        output_file = OUTPUT_DIR / "mean_filter_3x3.jpg"

        save_image(
            mean_result,
            str(output_file)
        )

        print(f"[OK] Đã lưu: {output_file}")

    except Exception as e:

        print(f"[ERROR] Mean Filter: {e}")


    # ========================================================
    # 2. GAUSSIAN FILTER
    # ========================================================

    print("\n[2/3] Đang chạy Gaussian Filter...")

    try:

        gaussian_result = gaussian_filter(
            image,
            kernel_size=5,
            sigma=1.0
        )

        output_file = OUTPUT_DIR / "gaussian_filter_5x5.jpg"

        save_image(
            gaussian_result,
            str(output_file)
        )

        print(f"[OK] Đã lưu: {output_file}")

    except Exception as e:

        print(f"[ERROR] Gaussian Filter: {e}")


    # ========================================================
    # 3. SHARPENING
    # ========================================================

    print("\n[3/3] Đang chạy Sharpening...")

    try:

        sharpening_result = sharpening(image)

        output_file = OUTPUT_DIR / "sharpening.jpg"

        save_image(
            sharpening_result,
            str(output_file)
        )

        print(f"[OK] Đã lưu: {output_file}")

    except Exception as e:

        print(f"[ERROR] Sharpening: {e}")


    # ========================================================
    # HOÀN THÀNH
    # ========================================================

    print("\n" + "=" * 60)
    print("          HOÀN THÀNH LINEAR FILTERS")
    print("=" * 60)

    print("\nCác kết quả được lưu tại:")

    print(OUTPUT_DIR)


# ============================================================
# 6. CHẠY CHƯƠNG TRÌNH
# ============================================================

if __name__ == "__main__":
    main()