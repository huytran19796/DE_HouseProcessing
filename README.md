# BUILDING ETL PROCESS WITH DATA ABOUT HOUSES AND APARTMENTS IN CALIFORNIA

## 1. OVERVIEW
- Hình ảnh
- Crawling: Dữ liệu về nhà ở và chung cư được triết xuất từ website www.zillow.com. Spiders được xây dựng bằng thư viện Scrapy
- Hình ảnh
- Transform Data: Dữ liệu thô sau khi được cào, cần được transform để làm sạch trước khi được đưa vào data warehouse.
- Load Data: Thiết kế các bảng Dimmension và Fact để phục vụ cho các yêu cầu cần phân tích. Cụ thể dữ liệu được đưa vào MySQL và được đưa vào S3 - AWS Redshift
- Hình ảnh
- Visualize Data: Thiết lập kết nối tới Redshift để lấy dữ liệu. Thực hiện các bài báo cáo đơn giản.
- Hình ảnh

## 2. SKILLS AND TOOLS
- Quá trình ETL được thực hiện dưới dạng các Tasks, TaskGroup trong Apache Airflow
- Data Warehouse: MySQL, AWS Redshift
- Libraries, Tools, other: Scrapy, Pandas, Docker, Python

## 3. CẤU TRÚC SOURCODE
.
    ├── ...
    ├── docs                    # Documentation files (alternatively `doc`)
    │   ├── TOC.md              # Table of contents
    │   ├── faq.md              # Frequently asked questions
    │   ├── misc.md             # Miscellaneous information
    │   ├── usage.md            # Getting started guide
    │   └── ...                 # etc.
    └── ...
