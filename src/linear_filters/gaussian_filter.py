import cv2

def gaussian_filter(image, kernel_size=5, sigma=1.0):
    if image is None:
        raise ValueError("Ảnh đầu vào không hợp lệ.")
    
    # Đảm bảo kernel_size là tuple số lẻ
    if isinstance(kernel_size, int):
        kernel_size = (kernel_size, kernel_size)

    return cv2.GaussianBlur(image, kernel_size, sigmaX=sigma)