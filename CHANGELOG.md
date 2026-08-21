Tất cả các thay đổi đáng chú ý của project Image Processing Lab 02 – Point Operations & Linear Filters sẽ được ghi lại trong file này.

Định dạng phiên bản sử dụng:

Added: chức năng mới

Changed: thay đổi chức năng hoặc cấu trúc

Fixed: sửa lỗi

Removed: loại bỏ chức năng

Documentation: cập nhật tài liệu

[Unreleased]

Added

Hoàn thiện các chức năng xử lý ảnh còn lại của bài thực hành.

Bổ sung kết quả thực nghiệm và hình ảnh minh họa.

Bổ sung các bài kiểm thử cho các module xử lý ảnh.

Changed

Tiếp tục hoàn thiện cấu trúc project và tích hợp các module.

Documentation

Cập nhật README.md.

Hoàn thiện tài liệu trong thư mục docs/.

[0.1.0] – Khởi tạo project

Added

Tạo cấu trúc project cho bài thực hành Chương 2 môn Xử lý ảnh và Thị giác máy tính.

Tạo thư mục data/ để quản lý ảnh đầu vào và ảnh kết quả.

Tạo thư mục src/ chứa source code chính.

Tạo module io/ phục vụ đọc và ghi ảnh.

Tạo nhóm point_operations/ cho các phép toán điểm ảnh.

Tạo nhóm linear_filters/ cho các bộ lọc tuyến tính.

Tạo nhóm advanced/ cho các bài tập xử lý ảnh nâng cao.

Tạo thư mục utils/ cho các chức năng dùng chung.

Tạo thư mục tests/ cho kiểm thử.

Tạo thư mục scripts/ cho các chương trình chạy từng nhóm chức năng.

Tạo thư mục notebooks/ cho thử nghiệm và phân tích.

Tạo thư mục docs/ cho tài liệu project.

Point Operations

Chuẩn bị module brightness.py cho chức năng tăng/giảm độ sáng.

Chuẩn bị module contrast.py cho chức năng thay đổi độ tương phản.

Chuẩn bị module negative.py cho biến đổi ảnh âm bản.

Chuẩn bị module threshold.py cho cắt ngưỡng và tạo ảnh nhị phân.

Linear Filters

Chuẩn bị module mean_filter.py cho lọc trung bình.

Chuẩn bị module gaussian_filter.py cho lọc Gaussian.

Chuẩn bị module sharpening.py cho làm sắc nét.

Advanced

Chuẩn bị module edge_detection.py cho phát hiện cạnh bằng Sobel và Prewitt.

Chuẩn bị module custom_kernel.py cho kernel tùy chỉnh.

Chuẩn bị module filter_comparison.py cho so sánh các bộ lọc.

Chuẩn bị module nonlinear_filter.py cho các bộ lọc phi tuyến.

Testing

Chuẩn bị các file test cho Brightness, Contrast, Negative và Threshold.

Chuẩn bị test cho Mean Filter, Gaussian Filter và Sharpening.

Documentation

Tạo README.md để giới thiệu project, hướng dẫn cài đặt và cách chạy.

Tạo requirements.txt để quản lý các thư viện Python cần thiết.

Chuẩn bị PLAN.md cho kế hoạch thực hiện.

Chuẩn bị REPORT.md cho báo cáo tổng hợp.

Chuẩn bị ALGORITHM.md cho phần lý thuyết và thuật toán.

Chuẩn bị RESULTS.md cho kết quả thực nghiệm và so sánh.

Quy ước cập nhật Changelog

Khi nhóm hoàn thành một chức năng, nên cập nhật file này.

Ví dụ:

## [0.2.0] – YYYY-MM-DD

### Added
- Hoàn thành Mean Filter.
- Hoàn thành Gaussian Filter.

### Fixed
- Sửa lỗi xử lý ảnh đầu vào không hợp lệ.

### Documentation
- Bổ sung kết quả Mean Filter vào RESULTS.md.

Mỗi thành viên nên cập nhật Changelog khi thực hiện một thay đổi đáng chú ý để nhóm có thể theo dõi lịch sử phát triển của project.