import pymysql
import csv

def load_fact_table():
    conn = pymysql.connect(
            host='mysql',
            user='airflow', 
            password = "airflow",
            db='airflow',
            )
    cur = conn.cursor()

    # Hands-on load fact_post table
    csv_data = csv.reader(open('/opt/airflow/data_stage_2/fact_post.csv'))
    next(csv_data)
    for row in csv_data:
        cur.execute('INSERT INTO fact_post(id, price, key_broker, key_province, key_house, status_type, status_text) VALUES(%s, %s, %s, %s, %s, %s, %s)',row)
    conn.commit()

    conn.close()