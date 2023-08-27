import pymysql
import csv

def load_dim_table():
    conn = pymysql.connect(
            host='mysql',
            user='airflow', 
            password = "airflow",
            db='airflow',
            )
    cur = conn.cursor()

    # Hands-on load dim_province table
    csv_data = csv.reader(open('/opt/airflow/data_stage_2/dim_province.csv'))
    next(csv_data)
    for row in csv_data:
        cur.execute('INSERT INTO dim_province(id,province) VALUES(%s, %s)',row)
    conn.commit()

    # Hands-on load dim_dstreet table
    csv_data = csv.reader(open('/opt/airflow/data_stage_2/dim_dstreet.csv'))
    next(csv_data)
    for row in csv_data:
        cur.execute('INSERT INTO dim_dstreet(id, number_street, key_province) VALUES(%s, %s, %s)',row)
    conn.commit()

    # Hands-on load dim_broker table
    csv_data = csv.reader(open('/opt/airflow/data_stage_2/dim_broker.csv'))
    next(csv_data)
    for row in csv_data:
        cur.execute('INSERT INTO dim_broker(id, broker_name) VALUES(%s, %s)',row)
    conn.commit()

    # Hands-on load dim_house table
    csv_data = csv.reader(open('/opt/airflow/data_stage_2/dim_house.csv'))
    next(csv_data)
    for row in csv_data:
        cur.execute('INSERT INTO dim_house(id_house, area, beds, baths, detail_url, image_url, id) VALUES(%s, %s, %s, %s, %s, %s, %s)',row)
    conn.commit()

    conn.close()