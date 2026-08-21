"""
run_point_operations.py

Chạy toàn bộ các phép toán điểm ảnh:
1. Brightness
2. Contrast
3. Negative
4. Threshold

Kết quả được lưu vào:
data/output/point_operations/
"""

import sys
from pathlib import Path

# ============================================================
# 1. XÁC ĐỊNH THƯ MỤC GỐC CỦA PROJECT
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Cho phép import các module trong src
sys.path.insert(0, str(PROJECT_ROOT))


# ============================================================
# 2. IMPORT CÁC MODULE
# ============================================================

from src.io.image_io import read_image, save_image

from src.point_operations.brightness import adjust_brightness
from src.point_operations.contrast import adjust_contrast
from src.point_operations.negative import negative
from src.point_operations.threshold import threshold


# ============================================================
# 3. CẤU HÌNH ĐƯỜNG DẪN
# ============================================================

INPUT_DIR = PROJECT_ROOT / "data" / "input"

OUTPUT_DIR = PROJECT_ROOT / "data" / "output" / "point_operations"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# 4. HÀM TÌM ẢNH ĐẦU VÀO
# ============================================================

def find_input_image():
    """
    Tìm ảnh đầu tiên trong thư mục data/input.
    Hỗ trợ các định dạng:
    .jpg, .jpeg, .png, .bmp
    """

    supported_formats = [".jpg", ".jpeg", ".png", ".bmp"]

    for file in INPUT_DIR.iterdir():
        if file.is_file() and file.suffix.lower() in supported_formats:
            return file

    return None


# ============================================================
# 5. CHƯƠNG TRÌNH CHÍNH
# ============================================================

def main():

    print("=" * 60)
    print("      POINT OPERATIONS - IMAGE PROCESSING LAB 02")
    print("=" * 60)

    # --------------------------------------------------------
    # Kiểm tra thư mục input
    # --------------------------------------------------------

    if not INPUT_DIR.exists():
        print(f"[ERROR] Không tìm thấy thư mục: {INPUT_DIR}")
        return

    # --------------------------------------------------------
    # Tìm ảnh đầu vào
    # --------------------------------------------------------

    input_file = find_input_image()

    if input_file is None:
        print("[ERROR] Không tìm thấy ảnh trong data/input/")
        print("Vui lòng thêm ảnh .jpg, .jpeg, .png hoặc .bmp")
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
    # 1. BRIGHTNESS
    # ========================================================

    print("\n[1/4] Đang xử lý Brightness...")

    try:
        bright_image = adjust_brightness(image, 50)

        output_file = OUTPUT_DIR / "brightness_plus_50.jpg"

        save_image(bright_image, str(output_file))

        print(f"[OK] Đã lưu: {output_file}")

    except Exception as e:
        print(f"[ERROR] Brightness: {e}")

    # ========================================================
    # 2. CONTRAST
    # ========================================================

    print("\n[2/4] Đang xử lý Contrast...")

    try:
        contrast_image = adjust_contrast(image, 1.5)

        output_file = OUTPUT_DIR / "contrast_1.5.jpg"

        save_image(contrast_image, str(output_file))

        print(f"[OK] Đã lưu: {output_file}")

    except Exception as e:
        print(f"[ERROR] Contrast: {e}")

    # ========================================================
    # 3. NEGATIVE
    # ========================================================

    print("\n[3/4] Đang xử lý Negative...")

    try:
        negative_image = negative(image)

        output_file = OUTPUT_DIR / "negative.jpg"

        save_image(negative_image, str(output_file))

        print(f"[OK] Đã lưu: {output_file}")

    except Exception as e:
        print(f"[ERROR] Negative: {e}")

    # ========================================================
    # 4. THRESHOLD
    # ========================================================

    print("\n[4/4] Đang xử lý Threshold...")

    try:
        threshold_image = threshold(image, 128)

        output_file = OUTPUT_DIR / "threshold_128.jpg"

        save_image(threshold_image, str(output_file))

        print(f"[OK] Đã lưu: {output_file}")

    except Exception as e:
        print(f"[ERROR] Threshold: {e}")

    # ========================================================
    # HOÀN THÀNH
    # ========================================================

    print("\n" + "=" * 60)
    print("          HOÀN THÀNH POINT OPERATIONS")
    print("=" * 60)

    print(f"\nKết quả được lưu tại:")
    print(OUTPUT_DIR)


# ============================================================
# 6. CHẠY CHƯƠNG TRÌNH
# ============================================================

if __name__ == "__main__":
    main()