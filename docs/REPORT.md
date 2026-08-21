# REPORT.md

# BÁO CÁO BÀI THỰC HÀNH CHƯƠNG 2
## XỬ LÝ ẢNH VÀ THỊ GIÁC MÁY TÍNH

### Image Processing Lab 02 – Point Operations & Linear Filters

---

## 1. GIỚI THIỆU

### 1.1. Mục đích

Bài thực hành nhằm giúp sinh viên làm quen với các kỹ thuật xử lý ảnh cơ bản và áp dụng chúng vào chương trình Python.

Các nội dung được thực hiện gồm:

- Các toán tử điểm ảnh.
- Các bộ lọc tuyến tính.
- Các phương pháp phát hiện cạnh.
- Thiết kế kernel tùy chỉnh.
- So sánh các bộ lọc.
- Các bộ lọc phi tuyến.

Project được tổ chức thành nhiều module độc lập nhằm giúp việc phát triển, kiểm thử và tích hợp dễ dàng hơn.

---

## 2. MỤC TIÊU

Project hướng đến các mục tiêu sau:

1. Đọc ảnh từ máy tính.
2. Hiểu cách biểu diễn ảnh dưới dạng ma trận điểm ảnh.
3. Thực hiện các phép biến đổi trực tiếp trên giá trị pixel.
4. Áp dụng các bộ lọc để làm mờ và làm sắc nét ảnh.
5. Phát hiện các cạnh trong ảnh.
6. Thiết kế và thử nghiệm kernel tùy chỉnh.
7. So sánh hiệu quả của các phương pháp xử lý ảnh.
8. Tìm hiểu và áp dụng một số bộ lọc phi tuyến.
9. Kiểm thử các chức năng đã xây dựng.
10. Phân tích kết quả thông qua ảnh đầu vào và ảnh sau xử lý.

---

# 3. CẤU TRÚC PROJECT

Project được tổ chức thành các thành phần chính:

```text
ImageProcessing_Lab02_PointOps_LinearFilters/
│
├── README.md
├── CHANGELOG.md
├── LICENSE
├── requirements.txt
│
├── docs/
│   ├── PLAN.md
│   ├── REPORT.md
│   ├── ALGORITHM.md
│   └── RESULTS.md
│
├── data/
│   ├── input/
│   └── output/
│       ├── point_operations/
│       ├── linear_filters/
│       └── advanced/
│
├── src/
│   ├── main.py
│   ├── io/
│   ├── point_operations/
│   ├── linear_filters/
│   ├── advanced/
│   └── utils/
│
├── tests/
├── scripts/
└── notebooks/