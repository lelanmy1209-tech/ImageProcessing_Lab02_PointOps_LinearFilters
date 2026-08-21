import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# HIỂN THỊ MỘT ẢNH
# ============================================================

def show_image(
    image,
    title="Image",
    cmap=None,
    figsize=(8, 6)
):
    """
    Hiển thị một ảnh.

    Parameters:
        image: Ảnh cần hiển thị.
        title: Tiêu đề ảnh.
        cmap: Colormap, ví dụ "gray".
        figsize: Kích thước hình.
    """

    if image is None:
        raise ValueError(
            "Ảnh đầu vào không hợp lệ."
        )

    plt.figure(figsize=figsize)

    # Nếu ảnh grayscale
    if image.ndim == 2:

        plt.imshow(
            image,
            cmap=cmap if cmap else "gray"
        )

    # Nếu ảnh màu
    elif image.ndim == 3:

        plt.imshow(image)

    else:
        raise ValueError(
            "Ảnh phải có 2 hoặc 3 chiều."
        )

    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


# ============================================================
# HIỂN THỊ ẢNH GỐC VÀ ẢNH KẾT QUẢ
# ============================================================

def compare_images(
    original,
    result,
    original_title="Original Image",
    result_title="Processed Image",
    figsize=(12, 5)
):
    """
    Hiển thị ảnh gốc và ảnh sau xử lý cạnh nhau.

    Parameters:
        original: Ảnh gốc.
        result: Ảnh sau xử lý.
        original_title: Tiêu đề ảnh gốc.
        result_title: Tiêu đề ảnh kết quả.
        figsize: Kích thước hình.
    """

    if original is None:
        raise ValueError(
            "Ảnh gốc không hợp lệ."
        )

    if result is None:
        raise ValueError(
            "Ảnh kết quả không hợp lệ."
        )

    plt.figure(figsize=figsize)

    # --------------------------------------------------------
    # ẢNH GỐC
    # --------------------------------------------------------

    plt.subplot(1, 2, 1)

    if original.ndim == 2:

        plt.imshow(
            original,
            cmap="gray"
        )

    else:

        plt.imshow(original)

    plt.title(original_title)
    plt.axis("off")

    # --------------------------------------------------------
    # ẢNH KẾT QUẢ
    # --------------------------------------------------------

    plt.subplot(1, 2, 2)

    if result.ndim == 2:

        plt.imshow(
            result,
            cmap="gray"
        )

    else:

        plt.imshow(result)

    plt.title(result_title)
    plt.axis("off")

    plt.tight_layout()
    plt.show()


# ============================================================
# HIỂN THỊ NHIỀU ẢNH
# ============================================================

def show_multiple_images(
    images,
    titles=None,
    figsize=(15, 8),
    cols=3
):
    """
    Hiển thị nhiều ảnh trên cùng một figure.

    Parameters:
        images: List các ảnh.
        titles: List tiêu đề.
        figsize: Kích thước figure.
        cols: Số cột.
    """

    if images is None or len(images) == 0:
        raise ValueError(
            "Danh sách ảnh không được rỗng."
        )

    if titles is not None:
        if len(titles) != len(images):
            raise ValueError(
                "Số lượng titles phải bằng số lượng images."
            )

    # Tính số hàng
    rows = int(
        np.ceil(len(images) / cols)
    )

    plt.figure(figsize=figsize)

    for i, image in enumerate(images):

        if image is None:
            continue

        plt.subplot(
            rows,
            cols,
            i + 1
        )

        # Ảnh grayscale
        if image.ndim == 2:

            plt.imshow(
                image,
                cmap="gray"
            )

        # Ảnh màu
        elif image.ndim == 3:

            plt.imshow(image)

        else:
            raise ValueError(
                "Ảnh phải có 2 hoặc 3 chiều."
            )

        # Tiêu đề
        if titles is not None:
            plt.title(titles[i])
        else:
            plt.title(
                f"Image {i + 1}"
            )

        plt.axis("off")

    plt.tight_layout()
    plt.show()


# ============================================================
# SO SÁNH CÁC BỘ LỌC
# ============================================================

def visualize_filter_results(
    original,
    results,
    figsize=(16, 10)
):
    """
    Hiển thị ảnh gốc và kết quả của nhiều bộ lọc.

    Parameters:
        original: Ảnh gốc.
        results: Dictionary chứa các ảnh kết quả.
        figsize: Kích thước figure.

    Ví dụ:
        results = {
            "Mean": mean_image,
            "Gaussian": gaussian_image,
            "Sharpening": sharpen_image
        }
    """

    if original is None:
        raise ValueError(
            "Ảnh gốc không hợp lệ."
        )

    if not isinstance(results, dict):
        raise TypeError(
            "results phải là dictionary."
        )

    # Tạo danh sách ảnh
    images = [original]

    titles = ["Original"]

    for name, image in results.items():

        if image is None:
            continue

        # Không hiển thị gradient nếu có
        if name.endswith("_x"):
            continue

        if name.endswith("_y"):
            continue

        images.append(image)
        titles.append(name)

    # Hiển thị
    show_multiple_images(
        images,
        titles,
        figsize=figsize
    )


# ============================================================
# HIỂN THỊ KERNEL
# ============================================================

def show_kernel(
    kernel,
    title="Kernel",
    figsize=(5, 5)
):
    """
    Hiển thị kernel dưới dạng ma trận màu.

    Parameters:
        kernel: Kernel xử lý ảnh.
        title: Tiêu đề.
        figsize: Kích thước figure.
    """

    if kernel is None:
        raise ValueError(
            "Kernel không hợp lệ."
        )

    kernel = np.asarray(
        kernel,
        dtype=np.float64
    )

    if kernel.ndim != 2:
        raise ValueError(
            "Kernel phải là ma trận 2 chiều."
        )

    plt.figure(figsize=figsize)

    plt.imshow(
        kernel,
        cmap="gray"
    )

    plt.title(title)
    plt.colorbar()

    plt.xticks(
        range(kernel.shape[1])
    )

    plt.yticks(
        range(kernel.shape[0])
    )

    # Hiển thị giá trị trên kernel
    for i in range(kernel.shape[0]):

        for j in range(kernel.shape[1]):

            plt.text(
                j,
                i,
                f"{kernel[i, j]:.2f}",
                ha="center",
                va="center"
            )

    plt.tight_layout()
    plt.show()


# ============================================================
# HIỂN THỊ GRADIENT X VÀ Y
# ============================================================

def visualize_gradients(
    gradient_x,
    gradient_y,
    magnitude,
    figsize=(15, 5)
):
    """
    Hiển thị Gradient X, Gradient Y
    và độ lớn Gradient.

    Parameters:
        gradient_x: Gradient theo X.
        gradient_y: Gradient theo Y.
        magnitude: Độ lớn gradient.
        figsize: Kích thước figure.
    """

    if gradient_x is None:
        raise ValueError(
            "gradient_x không hợp lệ."
        )

    if gradient_y is None:
        raise ValueError(
            "gradient_y không hợp lệ."
        )

    if magnitude is None:
        raise ValueError(
            "magnitude không hợp lệ."
        )

    plt.figure(figsize=figsize)

    # Gradient X
    plt.subplot(1, 3, 1)

    plt.imshow(
        gradient_x,
        cmap="gray"
    )

    plt.title("Gradient X")
    plt.axis("off")

    # Gradient Y
    plt.subplot(1, 3, 2)

    plt.imshow(
        gradient_y,
        cmap="gray"
    )

    plt.title("Gradient Y")
    plt.axis("off")

    # Magnitude
    plt.subplot(1, 3, 3)

    plt.imshow(
        magnitude,
        cmap="gray"
    )

    plt.title("Gradient Magnitude")
    plt.axis("off")

    plt.tight_layout()
    plt.show()


# ============================================================
# LƯU FIGURE
# ============================================================

def save_figure(
    filename,
    dpi=300,
    bbox_inches="tight"
):
    """
    Lưu figure hiện tại thành file ảnh.

    Parameters:
        filename: Đường dẫn file cần lưu.
        dpi: Độ phân giải.
        bbox_inches: Căn chỉnh vùng lưu.
    """

    if not filename:
        raise ValueError(
            "filename không được để trống."
        )

    plt.savefig(
        filename,
        dpi=dpi,
        bbox_inches=bbox_inches
    )


# ============================================================
# LƯU SO SÁNH NHIỀU ẢNH
# ============================================================

def save_comparison(
    original,
    results,
    filename,
    figsize=(16, 10),
    dpi=300
):
    """
    Hiển thị và lưu kết quả so sánh.

    Parameters:
        original: Ảnh gốc.
        results: Dictionary kết quả.
        filename: Đường dẫn file output.
        figsize: Kích thước figure.
        dpi: Độ phân giải.
    """

    if original is None:
        raise ValueError(
            "Ảnh gốc không hợp lệ."
        )

    if not isinstance(results, dict):
        raise TypeError(
            "results phải là dictionary."
        )

    images = [original]
    titles = ["Original"]

    for name, image in results.items():

        if image is None:
            continue

        if name.endswith("_x"):
            continue

        if name.endswith("_y"):
            continue

        images.append(image)
        titles.append(name)

    rows = int(
        np.ceil(len(images) / 3)
    )

    plt.figure(
        figsize=figsize
    )

    for i, image in enumerate(images):

        plt.subplot(
            rows,
            3,
            i + 1
        )

        if image.ndim == 2:

            plt.imshow(
                image,
                cmap="gray"
            )

        else:

            plt.imshow(image)

        plt.title(
            titles[i]
        )

        plt.axis("off")

    plt.tight_layout()

    plt.savefig(
        filename,
        dpi=dpi,
        bbox_inches="tight"
    )

    plt.show()