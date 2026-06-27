# HƯỚNG DẪN SỬ DỤNG CHƯƠNG TRÌNH

## 1. Giới thiệu

Tài liệu này hướng dẫn cài đặt, triển khai và sử dụng hệ thống phân tích dữ liệu bán hàng sử dụng Business Intelligence.

## 2. Yêu cầu hệ thống

### Phần cứng

* CPU Intel Core i3 hoặc cao hơn.
* RAM tối thiểu 8 GB.
* Dung lượng ổ cứng trống tối thiểu 5 GB.

### Phần mềm

* Windows 10/11.
* Python 3.11 hoặc mới hơn.
* Microsoft SQL Server 2022.
* SQL Server Management Studio (SSMS).
* Microsoft Power BI Desktop.

## 3. Chuẩn bị dữ liệu

Bộ dữ liệu được sử dụng là **Sales Forecasting Dataset** tải từ Kaggle.

Đặt file `train.csv` vào thư mục:

```text
dataset/
```

## 4. Tạo cơ sở dữ liệu

Mở SQL Server Management Studio và tạo Database:

```sql
CREATE DATABASE SalesDataWarehouse;
```

Tiếp theo thực hiện các file SQL trong thư mục `sql/` để tạo các bảng của hệ thống.

## 5. Chạy chương trình ETL

Mở Command Prompt hoặc PowerShell tại thư mục dự án và thực hiện:

```bash
python etl/etl.py
```

Nếu chương trình chạy thành công sẽ hiển thị:

```text
DimCustomer inserted successfully!
DimProduct inserted successfully!
DimTime inserted successfully!
DimLocation inserted successfully!
FactSales inserted successfully!
ETL completed successfully!
```

Kiểm tra trong SQL Server sẽ thấy các bảng:

* FactSales
* DimCustomer
* DimProduct
* DimTime
* DimLocation

đã được nạp dữ liệu.

## 6. Mở Dashboard

* Khởi động Microsoft Power BI Desktop.
* Mở file Dashboard (.pbix).
* Chọn **Refresh** để đồng bộ dữ liệu từ SQL Server.
* Dashboard sẽ hiển thị các biểu đồ và KPI.

## 7. Chạy demo

Quy trình chạy demo gồm các bước sau:

1. Mở SQL Server và kiểm tra cơ sở dữ liệu.
2. Chạy chương trình ETL bằng Python.
3. Kiểm tra dữ liệu đã được nạp vào các bảng.
4. Mở Power BI Desktop.
5. Refresh dữ liệu.
6. Quan sát Dashboard và thực hiện các thao tác lọc dữ liệu theo thời gian, khu vực, sản phẩm hoặc khách hàng.

## 8. Kết quả mong đợi

Sau khi hoàn thành các bước trên, hệ thống sẽ:

* Hoàn thành quá trình ETL.
* Dữ liệu được lưu trong Data Warehouse.
* Dashboard Power BI hiển thị đầy đủ KPI và biểu đồ phân tích.
* Người dùng có thể theo dõi doanh thu theo thời gian, khu vực, khách hàng và sản phẩm.

## 9. Một số lỗi thường gặp

**Không kết nối được SQL Server**

* Kiểm tra SQL Server đã khởi động.
* Kiểm tra tên Server trong file cấu hình.

**Lỗi thiếu thư viện Python**

```bash
pip install -r requirements.txt
```

**Power BI không hiển thị dữ liệu**

* Kiểm tra kết nối SQL Server.
* Chọn Refresh để cập nhật dữ liệu.
* Kiểm tra dữ liệu đã được nạp thành công sau khi chạy ETL.
