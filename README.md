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
```
|   .env
|   docker-compose.yaml
|   README.md
|
+---crawling
|   |   run_spider.py
|   |   scrapy.cfg
|   |
|   \---zillow
|       |   items.py
|       |   middlewares.py
|       |   pipelines.py
|       |   settings.py
|       |   utils.py
|       |   __init__.py
|       |
|       \---spiders
|           |   zillow_house.py
|           |   __init__.py
|           |
|           \---__pycache__
|                   zillow_house.cpython-310.pyc
|                   zillow_house.cpython-37.pyc
|                   __init__.cpython-310.pyc
|                   __init__.cpython-37.pyc
|
+---dags
|   |   houses_processing.py
|   |
|   \---group_task
|       |   cloud_tasks.py
|       |   mysql_tasks.py
|       |   transform_tasks.py
|       |
|       \---__pycache__
|               cloud_tasks.cpython-37.pyc
|               mysql_tasks.cpython-37.pyc
|               transform_tasks.cpython-37.pyc
|
+---data_stage_1
|       california_houses.json
|
+---data_stage_2
|       dim_broker.csv
|       dim_dstreet.csv
|       dim_house.csv
|       dim_province.csv
|       fact_post.csv
|
+---data_transform
|       transform.py
|       transform_dim_address.py
|       transform_dim_broker.py
|       transform_dim_house.py
|       transform_fact_post.py
|
+---logs
+---mysql_utils
|       load_dim_table.py
|       load_fact_table.py
|       set_up_database.sql
|
+---plugins
\---redshift_utils
        aws_infor.py
        load_local_to_s3.py
        load_s3_to_redshift.py
        set_up_database.sql
```
