import pandas as pd

class Transform:
    def __init__(self, keep_columns=None):
        self.path = '/opt/airflow/data_stage_1/california_houses.json'
        
        if keep_columns:
            self.df = pd.read_json(self.path)[keep_columns]
        else:
            self.df = pd.read_json(self.path)
        
        self.path_dim_province = '/opt/airflow/data_stage_2/dim_province.csv'
        self.path_dim_dstreet = '/opt/airflow/data_stage_2/dim_dstreet.csv'
        self.path_dim_broker = '/opt/airflow/data_stage_2/dim_broker.csv'
        self.path_dim_house = '/opt/airflow/data_stage_2/dim_house.csv'
        self.path_fact_post = '/opt/airflow/data_stage_2/fact_post.csv'
    
    def cleaning(self, column_name):
        self.df.dropna(subset=[column_name], inplace=True)
    
    def reduplicate(self, column_name):
        self.df.drop_duplicates(subset=[column_name], keep='first', inplace=True, ignore_index=True)

    def formating(self):
        pass

    def gen_id_key(self):
        pass

    def write_csv(self, df, path):
        df.to_csv(path, index = False)
    
    def print(self):
        print(self.df)