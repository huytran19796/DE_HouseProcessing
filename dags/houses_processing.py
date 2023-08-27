import sys
sys.path.append('/opt/airflow')
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import  PythonOperator
from group_task.transform_tasks import transform_task
from group_task.mysql_tasks import mysql_task
from group_task.cloud_tasks import cloud_task
from datetime import datetime

def run_scrapy_spider():
    import subprocess
    result = subprocess.Popen(["python", "crawling/run_spider.py"])
    result.communicate()  # Đợi cho tiến trình kết thúc

default_args={
    "mysql_conn_id": "mysql_connect"
    }

with DAG(
    'houses_processing', 
    default_args = default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    template_searchpath = ['/opt/airflow/mysql_utils/', '/opt/airflow/redshift_utils/']
    ) as dag:
    
    start = DummyOperator(task_id='start')
    end = DummyOperator(task_id='end')

    crawl_data = PythonOperator(
        task_id = 'crawl_data',
        python_callable = run_scrapy_spider,
    )

    transform_data = transform_task()
    mysql_process = mysql_task()
    cloud_process = cloud_task()
    
    start >> crawl_data >> transform_data >> [mysql_process, cloud_process] >> end