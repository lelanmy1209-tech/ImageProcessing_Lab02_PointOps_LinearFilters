import cv2
import os


def read_image(image_path):
    """
    Đọc ảnh từ đường dẫn.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Không tìm thấy ảnh: {image_path}")

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Không thể đọc ảnh: {image_path}")

    return image


def save_image(image, output_path):
    """
    Lưu ảnh vào đường dẫn chỉ định.
    """
    output_dir = os.path.dirname(output_path)

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    success = cv2.imwrite(output_path, image)

    if not success:
        raise ValueError(f"Không thể lưu ảnh: {output_path}")

    return output_path


def get_image_size(image):
    """
    Lấy kích thước ảnh.
    Trả về: width, height, channels
    """
    height, width = image.shape[:2]

    if len(image.shape) == 3:
        channels = image.shape[2]
    else:
        channels = 1

    return width, height, channels