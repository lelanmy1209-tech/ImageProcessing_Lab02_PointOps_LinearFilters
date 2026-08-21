import numpy as np

from src.point_operations.negative import negative


# ============================================================
# TEST ĐẢO ẢNH CƠ BẢN
# ============================================================

def test_negative_basic():
    """
    Kiểm tra phép negative với các giá trị pixel cơ bản.
    """

    image = np.array(
        [
            [0, 50],
            [100, 255]
        ],
        dtype=np.uint8
    )

    result = negative(image)

    expected = np.array(
        [
            [255, 205],
            [155, 0]
        ],
        dtype=np.uint8
    )

    assert np.array_equal(
        result,
        expected
    )


# ============================================================
# TEST PIXEL 0
# ============================================================

def test_negative_zero():
    """
    Pixel 0 sau khi negative phải thành 255.
    """

    image = np.array(
        [[0]],
        dtype=np.uint8
    )

    result = negative(image)

    assert result[0, 0] == 255


# ============================================================
# TEST PIXEL 255
# ============================================================

def test_negative_255():
    """
    Pixel 255 sau khi negative phải thành 0.
    """

    image = np.array(
        [[255]],
        dtype=np.uint8
    )

    result = negative(image)

    assert result[0, 0] == 0


# ============================================================
# TEST PIXEL 128
# ============================================================

def test_negative_middle_value():
    """
    Kiểm tra pixel ở giữa khoảng [0, 255].
    """

    image = np.array(
        [[128]],
        dtype=np.uint8
    )

    result = negative(image)

    assert result[0, 0] == 127


# ============================================================
# TEST TÍNH ĐẢO NGƯỢC
# ============================================================

def test_negative_inverse():
    """
    Áp dụng negative hai lần phải thu được
    ảnh ban đầu.
    """

    image = np.array(
        [
            [0, 25, 50],
            [100, 150, 200],
            [225, 250, 255]
        ],
        dtype=np.uint8
    )

    result = negative(
        negative(image)
    )

    assert np.array_equal(
        result,
        image
    )


# ============================================================
# TEST ẢNH GRAYSCALE
# ============================================================

def test_negative_grayscale():
    """
    Kiểm tra negative với ảnh grayscale.
    """

    image = np.array(
        [
            [20, 60],
            [120, 200]
        ],
        dtype=np.uint8
    )

    result = negative(image)

    expected = np.array(
        [
            [235, 195],
            [135, 55]
        ],
        dtype=np.uint8
    )

    assert np.array_equal(
        result,
        expected
    )


# ============================================================
# TEST ẢNH MÀU
# ============================================================

def test_negative_color():
    """
    Kiểm tra negative với ảnh màu RGB.

    Mỗi channel được đảo riêng:
        R -> 255 - R
        G -> 255 - G
        B -> 255 - B
    """

    image = np.array(
        [
            [
                [0, 50, 100],
                [150, 200, 255]
            ]
        ],
        dtype=np.uint8
    )

    result = negative(image)

    expected = np.array(
        [
            [
                [255, 205, 155],
                [105, 55, 0]
            ]
        ],
        dtype=np.uint8
    )

    assert np.array_equal(
        result,
        expected
    )


# ============================================================
# TEST KIỂU DỮ LIỆU
# ============================================================

def test_negative_output_dtype():
    """
    Kết quả phải có kiểu dữ liệu uint8.
    """

    image = np.array(
        [
            [10, 50],
            [100, 200]
        ],
        dtype=np.uint8
    )

    result = negative(image)

    assert result.dtype == np.uint8


# ============================================================
# TEST KÍCH THƯỚC ẢNH
# ============================================================

def test_negative_shape():
    """
    Kích thước ảnh sau khi xử lý
    phải giống ảnh ban đầu.
    """

    image = np.zeros(
        (10, 20),
        dtype=np.uint8
    )

    result = negative(image)

    assert result.shape == image.shape


# ============================================================
# TEST TOÀN BỘ DẢI PIXEL
# ============================================================

def test_negative_full_range():
    """
    Kiểm tra toàn bộ giá trị pixel từ 0 đến 255.
    """

    image = np.arange(
        256,
        dtype=np.uint8
    )

    result = negative(image)

    expected = 255 - image

    assert np.array_equal(
        result,
        expected
    )