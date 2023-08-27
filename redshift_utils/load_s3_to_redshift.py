import redshift_connector
import redshift_utils.aws_infor as aws_infor

# Configure database credentials
conn = redshift_connector.connect(
    iam = True,
    region = aws_infor.region,
    cluster_identifier = aws_infor.cluster_identifier ,
    database= aws_infor.database,
    db_user= aws_infor.db_user,
    password= aws_infor.password,
    access_key_id = aws_infor.access_key,
    secret_access_key = aws_infor.secret_key,
    port = aws_infor.port
    )
conn.autocommit = True

def set_up_redshift():
    sql_file = "/opt/airflow/redshift_utils/set_up_database.sql"

    # Create a Cursor object
    cursor = conn.cursor()

    commands = None
    with open(sql_file, encoding="utf-8") as f:
        commands = f.read().split(';')
    
    # Execute script
    if commands:
        for command in commands:
            cursor.execute(command)
            print(command)
    
    cursor.close()
    conn.close()

def load_data_to_redshift():
    cursor = conn.cursor()
    names = ['dim_broker', 'dim_province', 'dim_dstreet', 'dim_house', 'fact_post']
    for name in names:
        statement = f"""
                COPY house_procesing.{name}
                FROM 's3://{aws_infor.s3_bucket_name}/{name}.csv'
                credentials 'aws_access_key_id={aws_infor.access_key};aws_secret_access_key={aws_infor.secret_key}'
                FORMAT AS CSV
                IGNOREHEADER 1
                FILLRECORD;
            """
        cursor.execute(statement)