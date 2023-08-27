from airflow.utils.task_group import TaskGroup
from airflow.operators.python import PythonOperator
from redshift_utils.load_local_to_s3 import load_to_s3
from redshift_utils.load_s3_to_redshift import set_up_redshift, load_data_to_redshift

def cloud_task():
    with TaskGroup("awscloud-processing", tooltip="AWS process") as group:
        load_to_s3_task = PythonOperator(
        task_id = "load_to_s3",
        python_callable = load_to_s3
        )

        set_up_redshift_task = PythonOperator(
            task_id = "set_up_redshift",
            python_callable = set_up_redshift
        )

        load_data_to_redshift_task = PythonOperator(
            task_id = "load_data_to_redshift",
            python_callable = load_data_to_redshift
        )

        load_to_s3_task >> set_up_redshift_task >> load_data_to_redshift_task
        return group