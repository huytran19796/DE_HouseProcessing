import boto3
import redshift_utils.aws_infor as aws_infor

# Tạo client S3
s3 = boto3.client('s3', aws_access_key_id=aws_infor.access_key, aws_secret_access_key=aws_infor.secret_key)

def load_to_s3():
    s3_bucket_name = aws_infor.s3_bucket_name
    all_files = ["dim_broker.csv", "dim_dstreet.csv", "dim_house.csv", "dim_province.csv", "fact_post.csv"]

    for name in all_files:
        local_file_path = f"/opt/airflow/data_stage_2/{name}"
        s3_destination_path = name
        load_table(s3, s3_bucket_name, local_file_path, s3_destination_path)

def load_table(connect, bucket_name, path_file, destination_s3):
    try:
        connect.head_object(Bucket=bucket_name, Key=destination_s3)
        print("File exists on S3. Deleting...")
        connect.delete_object(Bucket=bucket_name, Key=destination_s3)
    except:
        print("File does not exist on S3.")

    connect.upload_file(path_file, bucket_name, destination_s3)