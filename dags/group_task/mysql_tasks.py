from airflow.utils.task_group import TaskGroup
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator
from mysql_utils.load_dim_table import load_dim_table
from mysql_utils.load_fact_table import load_fact_table

def mysql_task():
    with TaskGroup("mysql-processing", tooltip="MySQL process") as group:
        set_up_database_task = MySqlOperator(
            task_id = 'set_up_database',
            sql = 'set_up_database.sql'
        )

        load_dim_table_task = PythonOperator(
            task_id = "load_dim_table",
            python_callable = load_dim_table
        )

        load_fact_table_task = PythonOperator(
            task_id = "load_fact_table",
            python_callable = load_fact_table
        )

        set_up_database_task >> load_dim_table_task >> load_fact_table_task

        return group