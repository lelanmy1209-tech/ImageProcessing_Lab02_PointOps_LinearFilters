import cv2
import numpy as np
from pathlib import Path


def read_image(image_path):
    """
    Đọc ảnh hỗ trợ đường dẫn tiếng Việt có dấu.
    """
    path_str = str(image_path)
    
    # Kiểm tra file có tồn tại không trước khi đọc
    if not Path(path_str).is_file():
        raise FileNotFoundError(f"Thư mục không có file ảnh: {path_str}")

    image = cv2.imdecode(np.fromfile(path_str, dtype=np.uint8), cv2.IMREAD_COLOR)

    if image is None:
        raise ValueError(f"File ảnh bị hỏng hoặc không định dạng được: {path_str}")

    return image


def save_image(image, output_path):
    """
    Lưu ảnh hỗ trợ đường dẫn tiếng Việt có dấu.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    ext = path.suffix if path.suffix else ".jpg"
    is_success, buffer = cv2.imencode(ext, image)

    if is_success:
        with open(path, "wb") as f:
            buffer.tofile(f)
        print(f"Đã lưu: {path.name}")
        return True
    else:
        raise ValueError(f"Không thể lưu ảnh: {path}")