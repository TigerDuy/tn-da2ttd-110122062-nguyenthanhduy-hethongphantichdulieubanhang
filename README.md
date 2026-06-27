# Sales BI Project

# Thiết kế và triển khai hệ thống phân tích dữ liệu bán hàng sử dụng Business Intelligence

## Giới thiệu

Sales BI Project là đồ án tốt nghiệp được thực hiện với mục tiêu xây dựng một hệ thống phân tích dữ liệu bán hàng dựa trên nền tảng Business Intelligence (BI). Hệ thống thực hiện quá trình thu thập dữ liệu, xử lý dữ liệu bằng quy trình ETL, xây dựng Data Warehouse trên Microsoft SQL Server và trực quan hóa dữ liệu bằng Microsoft Power BI nhằm hỗ trợ doanh nghiệp theo dõi tình hình kinh doanh và đưa ra quyết định dựa trên dữ liệu.

## Mục tiêu

* Thu thập và xử lý dữ liệu bán hàng từ bộ dữ liệu Sales Forecasting Dataset.
* Xây dựng quy trình ETL bằng Python.
* Thiết kế và triển khai Data Warehouse theo mô hình Star Schema.
* Xây dựng Dashboard trực quan bằng Microsoft Power BI.
* Hỗ trợ phân tích doanh thu theo thời gian, khách hàng, sản phẩm và khu vực.

## Kiến trúc hệ thống

```text
Sales Forecasting Dataset (CSV)
              │
              ▼
      Python ETL Process
 (Extract - Transform - Load)
              │
              ▼
 SQL Server Data Warehouse
      (Star Schema)
              │
              ▼
   Power BI Dashboard
```

## Công nghệ sử dụng

| Công nghệ                    | Mục đích                |
| ---------------------------- | ----------------------- |
| Python                       | Thực hiện quy trình ETL |
| Pandas                       | Đọc và xử lý dữ liệu    |
| Microsoft SQL Server         | Xây dựng Data Warehouse |
| SQL Server Management Studio | Quản lý cơ sở dữ liệu   |
| Microsoft Power BI Desktop   | Trực quan hóa dữ liệu   |
| Git & GitHub                 | Quản lý mã nguồn        |

## Phần mềm cần thiết

Trước khi triển khai dự án cần cài đặt các phần mềm sau:

* Python 3.11 hoặc mới hơn
* Microsoft SQL Server 2022
* SQL Server Management Studio (SSMS)
* Microsoft Power BI Desktop
* Git (khuyến nghị)

## Cách triển khai

### Bước 1. Clone dự án

```bash
git clone https://github.com/<username>/<repository>.git
cd <repository>
```

### Bước 2. Cài đặt thư viện Python

```bash
pip install -r requirements.txt
```

### Bước 3. Tạo cơ sở dữ liệu

Tạo Database mới trên SQL Server với tên:

```text
SalesDataWarehouse
```

Sau đó chạy các file SQL trong thư mục `sql/`.

### Bước 4. Chạy chương trình ETL

```bash
python etl/etl.py
```

Nếu thành công sẽ hiển thị:

```text
DimCustomer inserted successfully!
DimProduct inserted successfully!
DimTime inserted successfully!
DimLocation inserted successfully!
FactSales inserted successfully!
ETL completed successfully!
```

### Bước 5. Mở Dashboard

* Mở Microsoft Power BI Desktop.
* Mở file Dashboard (.pbix).
* Chọn **Refresh** để cập nhật dữ liệu mới nhất.

## Dataset

Sales Forecasting Dataset

https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting

## Cấu trúc thư mục

```text
SalesBIProject
│
├── dataset/              # Dữ liệu đầu vào
├── docs/                 # Tài liệu hướng dẫn
├── etl/                  # Chương trình ETL
├── sql/                  # Script SQL
├── powerbi/              # File Power BI
└── README.md
```

## Hướng dẫn sử dụng

Tài liệu hướng dẫn sử dụng và chạy demo được lưu tại:

```text
docs/HuongDanSuDung.md
```

## Tác giả

Nguyễn Thanh Duy

Khóa luận tốt nghiệp

Ngành Công nghệ thông tin
