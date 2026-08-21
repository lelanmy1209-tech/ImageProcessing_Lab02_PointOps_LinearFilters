Image Processing Lab 02 – Point Operations & Linear Filters

1. Giới thiệu

Đây là project bài thực hành Chương 2 – Xử lý ảnh và Thị giác máy tính.

Project tập trung vào các kỹ thuật xử lý ảnh cơ bản gồm:

Toán tử điểm ảnh (Point Operations)

Lọc tuyến tính (Linear Filters)

Các bài tập xử lý ảnh nâng cao (Advanced Image Processing)

Mục tiêu của project là xây dựng các chương trình xử lý ảnh bằng Python, thực hiện từng thuật toán trên ảnh đầu vào, lưu kết quả và hỗ trợ so sánh, đánh giá kết quả.

2. Mục tiêu

Project được xây dựng nhằm:

Hiểu nguyên lý hoạt động của các phép toán điểm ảnh.

Thực hiện thay đổi độ sáng và độ tương phản của ảnh.

Thực hiện biến đổi ảnh âm bản.

Tạo ảnh nhị phân bằng phương pháp cắt ngưỡng.

Làm mờ ảnh bằng Mean Filter và Gaussian Filter.

Làm sắc nét và tăng cường chi tiết của ảnh.

Phát hiện cạnh bằng các kernel Sobel và Prewitt.

Tự thiết kế và áp dụng kernel xử lý ảnh.

So sánh kết quả của nhiều phương pháp lọc khác nhau.

Tìm hiểu và áp dụng các bộ lọc phi tuyến như Median Filter và Bilateral Filter.

Tổ chức source code thành các module độc lập, dễ kiểm tra và mở rộng.

3. Nội dung bài thực hành

3.1. Toán tử điểm ảnh

Phần I gồm 4 chức năng:

Chức năng

File

Mô tả

Brightness

brightness.py

Tăng hoặc giảm độ sáng của toàn bộ ảnh

Contrast

contrast.py

Tăng hoặc giảm độ tương phản

Negative

negative.py

Biến đổi ảnh thành ảnh âm bản

Threshold

threshold.py

Tạo ảnh nhị phân bằng phương pháp cắt ngưỡng

Brightness

Thay đổi độ sáng bằng cách cộng hoặc trừ một giá trị cố định vào các điểm ảnh.

Giá trị dương: ảnh sáng hơn.

Giá trị âm: ảnh tối hơn.

Contrast

Thay đổi độ tương phản bằng cách điều chỉnh khoảng cách của giá trị điểm ảnh so với mức trung tâm.

Contrast lớn hơn: các vùng sáng/tối được phân biệt rõ hơn.

Contrast nhỏ hơn: ảnh trở nên phẳng hơn.

Negative

Biến đổi mỗi điểm ảnh thành giá trị đối của nó.

Đối với ảnh mức xám 8-bit:

s = 255 - r

Trong đó:

r: giá trị điểm ảnh ban đầu.

s: giá trị điểm ảnh sau biến đổi.

Threshold

So sánh giá trị điểm ảnh với một ngưỡng xác định để tạo ảnh nhị phân.

Ví dụ:

pixel >= threshold  -> 255
pixel < threshold   -> 0

3.2. Lọc tuyến tính

Phần II gồm 3 chức năng:

Chức năng

File

Mô tả

Mean Filter

mean_filter.py

Làm mờ ảnh bằng giá trị trung bình trong vùng lân cận

Gaussian Filter

gaussian_filter.py

Làm mờ ảnh bằng kernel Gaussian

Sharpening

sharpening.py

Tăng cường cạnh và chi tiết của ảnh

Mean Filter

Mean Filter thay thế giá trị của điểm ảnh bằng giá trị trung bình của các điểm ảnh trong một vùng lân cận.

Ví dụ với kernel 3×3:

1/9 × [ 1  1  1
        1  1  1
        1  1  1 ]

Tác dụng chính:

Làm mờ ảnh.

Giảm một phần nhiễu.

Có thể làm mất các chi tiết nhỏ.

Gaussian Filter

Gaussian Filter sử dụng kernel Gaussian, trong đó các điểm ảnh gần tâm kernel có trọng số lớn hơn.

Tác dụng:

Làm mờ ảnh.

Giảm nhiễu.

Tạo hiệu ứng làm mờ tự nhiên hơn Mean Filter trong nhiều trường hợp.

Sharpening

Sharpening tăng cường sự khác biệt giữa các vùng ảnh để làm nổi bật cạnh và chi tiết.

Tác dụng:

Làm ảnh rõ hơn.

Tăng cường cạnh.

Làm nổi bật các chi tiết.

4. Bài tập nâng cao

Phần III gồm 4 chức năng:

Chức năng

File

Mô tả

Edge Detection

edge_detection.py

Phát hiện cạnh bằng Sobel và Prewitt

Custom Kernel

custom_kernel.py

Tự thiết kế và áp dụng kernel

Filter Comparison

filter_comparison.py

So sánh kết quả của các bộ lọc

Nonlinear Filter

nonlinear_filter.py

Áp dụng Median Filter và Bilateral Filter

Edge Detection

Sử dụng các kernel phát hiện cạnh như:

Sobel

Prewitt

Mục tiêu là xác định các vùng có sự thay đổi cường độ mạnh trong ảnh.

Custom Kernel

Cho phép tự thiết kế kernel để tạo ra các hiệu ứng xử lý ảnh khác nhau.

Quá trình thực hiện:

Ảnh đầu vào
    ↓
Thiết kế kernel
    ↓
Áp dụng kernel
    ↓
Ảnh kết quả

Filter Comparison

Thực hiện nhiều phương pháp lọc trên cùng một ảnh để so sánh.

Có thể so sánh theo:

Mức độ làm mờ.

Khả năng giữ chi tiết.

Khả năng giảm nhiễu.

Độ rõ của cạnh.

Thời gian xử lý.

Nonlinear Filter

Tìm hiểu các bộ lọc phi tuyến như:

Median Filter

Bilateral Filter

Các bộ lọc này được sử dụng để xử lý nhiễu và giữ lại các đặc trưng quan trọng của ảnh trong những trường hợp phù hợp.

5. Cấu trúc project

ImageProcessing_Lab02_PointOps_LinearFilters/
│
├── README.md
├── CHANGELOG.md
├── LICENSE
├── requirements.txt
├── .gitignore
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
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── io/
│   │   ├── __init__.py
│   │   └── image_io.py
│   │
│   ├── point_operations/
│   │   ├── __init__.py
│   │   ├── brightness.py
│   │   ├── contrast.py
│   │   ├── negative.py
│   │   └── threshold.py
│   │
│   ├── linear_filters/
│   │   ├── __init__.py
│   │   ├── mean_filter.py
│   │   ├── gaussian_filter.py
│   │   └── sharpening.py
│   │
│   ├── advanced/
│   │   ├── __init__.py
│   │   ├── edge_detection.py
│   │   ├── custom_kernel.py
│   │   ├── filter_comparison.py
│   │   └── nonlinear_filter.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── validation.py
│       ├── visualization.py
│       └── metrics.py
│
├── tests/
│   ├── test_brightness.py
│   ├── test_contrast.py
│   ├── test_negative.py
│   ├── test_threshold.py
│   ├── test_mean_filter.py
│   ├── test_gaussian_filter.py
│   └── test_sharpening.py
│
├── scripts/
│   ├── run_point_operations.py
│   ├── run_linear_filters.py
│   └── run_advanced.py
│
└── notebooks/
    └── experiments.ipynb

6. Ý nghĩa các thư mục

data/

Chứa dữ liệu ảnh.

data/input/: ảnh đầu vào.

data/output/: ảnh sau khi xử lý.

Kết quả được phân loại thành:

point_operations/

linear_filters/

advanced/

src/

Chứa source code chính của project.

src/io/

Xử lý việc đọc ảnh đầu vào và lưu ảnh kết quả.

File chính:

image_io.py

src/point_operations/

Chứa các thuật toán toán tử điểm ảnh.

src/linear_filters/

Chứa các bộ lọc tuyến tính.

src/advanced/

Chứa các bài tập xử lý ảnh nâng cao.

src/utils/

Chứa các chức năng dùng chung:

Kiểm tra dữ liệu và tham số.

Trực quan hóa kết quả.

Tính toán các chỉ số đánh giá.

tests/

Chứa các chương trình kiểm thử cho những chức năng đã triển khai.

scripts/

Chứa các script hỗ trợ chạy từng nhóm chức năng.

notebooks/

Chứa Jupyter Notebook phục vụ thử nghiệm và phân tích thuật toán.

docs/

Chứa tài liệu của project:

PLAN.md: kế hoạch thực hiện.

REPORT.md: báo cáo.

ALGORITHM.md: lý thuyết và thuật toán.

RESULTS.md: kết quả thực nghiệm và so sánh.

7. Yêu cầu môi trường

Project sử dụng Python.

Các thư viện cần thiết được liệt kê trong:

requirements.txt

Khuyến nghị sử dụng môi trường ảo để tránh xung đột thư viện.

8. Cài đặt

Bước 1: Clone project

git clone <LINK_GITHUB_CUA_NHOM>

Sau đó di chuyển vào thư mục project:

cd ImageProcessing_Lab02_PointOps_LinearFilters

Thay <LINK_GITHUB_CUA_NHOM> bằng link repository thực tế của nhóm.

Bước 2: Tạo môi trường ảo

Windows:

python -m venv venv

Kích hoạt:

venv\Scripts\activate

Bước 3: Cài đặt thư viện

pip install -r requirements.txt

9. Chuẩn bị ảnh đầu vào

Đặt ảnh cần xử lý vào:

data/input/

Ví dụ:

data/
└── input/
    └── input.jpg

Nên sử dụng một ảnh đầu vào chung khi so sánh các thuật toán để kết quả thực nghiệm có tính nhất quán.

10. Chạy project

Chạy chương trình chính

python src/main.py

Chạy nhóm Point Operations

python scripts/run_point_operations.py

Chạy nhóm Linear Filters

python scripts/run_linear_filters.py

Chạy nhóm Advanced

python scripts/run_advanced.py

11. Kết quả đầu ra

Các ảnh sau khi xử lý được lưu trong:

data/output/

Theo từng nhóm:

data/output/
├── point_operations/
├── linear_filters/
└── advanced/

Ví dụ:

data/output/
├── point_operations/
│   ├── brightness.jpg
│   ├── contrast.jpg
│   ├── negative.jpg
│   └── threshold.jpg
│
├── linear_filters/
│   ├── mean.jpg
│   ├── gaussian.jpg
│   └── sharpening.jpg
│
└── advanced/
    ├── edge_detection.jpg
    ├── custom_kernel.jpg
    ├── filter_comparison/
    └── nonlinear_filter/

Tên file thực tế có thể thay đổi tùy theo cách triển khai của nhóm.

12. Quy trình xử lý ảnh

Quy trình tổng quát của project:

            ẢNH ĐẦU VÀO
                 │
                 ▼
          Đọc ảnh từ máy tính
                 │
                 ▼
        ┌───────────────────┐
        │   Chọn thuật toán │
        └───────────────────┘
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
 Point Ops   Linear     Advanced
             Filters
       │         │         │
       └─────────┼─────────┘
                 ▼
          Xử lý hình ảnh
                 │
                 ▼
       Hiển thị / lưu kết quả
                 │
                 ▼
          Phân tích kết quả

13. Kiểm thử

Project có thư mục tests/ để kiểm thử các chức năng.

Ví dụ:

python -m pytest

Hoặc chạy từng file kiểm thử:

python tests/test_brightness.py
python tests/test_contrast.py
python tests/test_negative.py
python tests/test_threshold.py

Các test còn lại có thể được chạy tương tự.

14. So sánh kết quả

Để đánh giá các thuật toán, nhóm sử dụng cùng một ảnh đầu vào và thay đổi phương pháp xử lý.

Ví dụ:

So sánh Mean và Gaussian

Tiêu chí

Mean Filter

Gaussian Filter

Làm mờ

Có

Có

Giảm nhiễu

Có

Có

Trọng số kernel

Đồng đều

Theo phân bố Gaussian

Giữ chi tiết

Có thể làm mất chi tiết

Thường tự nhiên hơn

Mục đích

Làm mờ đơn giản

Làm mờ và giảm nhiễu

So sánh Sobel và Prewitt

Tiêu chí

Sobel

Prewitt

Phát hiện cạnh

Có

Có

Phát hiện thay đổi theo X/Y

Có

Có

Kernel

Có trọng số lớn hơn ở vùng trung tâm

Đơn giản hơn

Mục đích

Phát hiện cạnh

Phát hiện cạnh

Kết quả thực tế cần được nhóm kiểm tra trên cùng dữ liệu đầu vào trước khi đưa ra kết luận cuối cùng.

15. Phân công thành viên

STT

Thành viên

Nội dung phụ trách

1

Thành viên 1

Brightness + hỗ trợ đọc/ghi ảnh

2

Thành viên 2

Contrast + Negative

3

Thành viên 3

Threshold

4

Thành viên 4

Mean Filter + trực quan hóa

5

Thành viên 5

Gaussian Filter + Sharpening

6

Thành viên 6

Edge Detection + Custom Kernel

7

Thành viên 7

Filter Comparison + Nonlinear Filter + tích hợp project

Thay "Thành viên 1", "Thành viên 2", ... bằng tên thật của các thành viên trong nhóm.

16. Quy tắc làm việc nhóm

Để tránh xung đột code, nhóm nên thống nhất:

Mỗi thành viên phụ trách đúng module được phân công.

Không tự ý sửa code của thành viên khác nếu chưa trao đổi.

Dùng Git để quản lý phiên bản.

Mỗi chức năng cần được kiểm thử trước khi ghép vào project.

Sử dụng cùng ảnh đầu vào khi thực hiện các phép so sánh.

Kết quả thực nghiệm phải được lưu lại.

Mỗi thành viên phải hiểu và giải thích được phần mình thực hiện.

Trước khi nộp, cả nhóm chạy lại toàn bộ project để kiểm tra lỗi.

17. Git workflow đề xuất

Tạo branch riêng

Ví dụ:

git checkout -b feature/brightness

Sau khi hoàn thành:

git add .
git commit -m "Implement brightness operation"
git push origin feature/brightness

Sau đó tạo Pull Request để ghép vào branch chính.

Tên branch có thể đặt theo chức năng:

feature/brightness
feature/contrast-negative
feature/threshold
feature/mean-filter
feature/gaussian-sharpening
feature/edge-custom-kernel
feature/comparison-nonlinear

18. Tài liệu liên quan

Các tài liệu của project nằm trong thư mục docs/:

File

Nội dung

PLAN.md

Kế hoạch thực hiện project

REPORT.md

Báo cáo tổng hợp

ALGORITHM.md

Giải thích lý thuyết và thuật toán

RESULTS.md

Kết quả và phân tích thực nghiệm

19. Tác giả

Môn học: Xử lý ảnh và Thị giác máy tính

Bài thực hành: Chương 2

Tên project: Image Processing Lab 02 – Point Operations & Linear Filters

Nhóm: 5

Thành viên

[Họ và tên – MSSV]

[Họ và tên – MSSV]

[Họ và tên – MSSV]

[Họ và tên – MSSV]

[Họ và tên – MSSV]

[Họ và tên – MSSV]

[Họ và tên – MSSV]

20. Trạng thái project

Hoàn thành Point Operations

Hoàn thành Linear Filters

Hoàn thành Edge Detection

Hoàn thành Custom Kernel

Hoàn thành Filter Comparison

Hoàn thành Nonlinear Filter

Hoàn thành Unit Tests

Hoàn thành thực nghiệm

Hoàn thành phân tích kết quả

Hoàn thành báo cáo

Hoàn thành slide thuyết trình

21. Ghi chú

README này mô tả cấu trúc, mục tiêu, chức năng và cách sử dụng của project. Các thông số cụ thể của từng thuật toán, kết quả thực nghiệm và phân tích chi tiết nên được trình bày trong các tài liệu tương ứng trong thư mục docs/.

Project có thể được mở rộng thêm các thuật toán xử lý ảnh khác trong tương lai.#   I m a g e P r o c e s s i n g _ L a b 0 2 _ P o i n t O p s _ L i n e a r F i l t e r s  
 