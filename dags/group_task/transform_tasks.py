from airflow.utils.task_group import TaskGroup
from airflow.operators.python import PythonOperator, BranchPythonOperator
from data_transform.transform_fact_post import transform_fact_post
from data_transform.transform_dim_house import transform_dim_house
from data_transform.transform_dim_broker import transform_dim_broker
from data_transform.transform_dim_address import transform_dim_address

def transform_task():
    with TaskGroup("transform-data", tooltip="Transform Data") as group:
        transform_dim_address_task = PythonOperator(
            task_id = 'transform_dim_address',
            python_callable = transform_dim_address
        )
        
        transform_dim_broker_task = PythonOperator(
            task_id = 'transform_dim_broker',
            python_callable= transform_dim_broker
        )

        transform_dim_house_task = PythonOperator(
            task_id = 'transform_dim_house',
            python_callable = transform_dim_house
        )

        transform_fact_post_task = PythonOperator(
            task_id = 'transform_fact_post',
            python_callable = transform_fact_post
        )
        [transform_dim_address_task, transform_dim_broker_task, transform_dim_house_task] >> transform_fact_post_task
        return group