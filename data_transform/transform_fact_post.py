from data_transform.transform import Transform
import pandas as pd

class Transform_Dim_Post(Transform):
    def __init__(self, keep_columns=None):
        super().__init__(keep_columns)
    
    def do_transform(self):
        self.cleaning('id')
        self.reduplicate('id')
        self.df['broker_name'] = self.df['broker_name'].fillna("Zillow")
        self.df[['number-street', 'province', 'zipcode']] = self.df['address'].str.split(',', expand=True)

        # Hands-on dim_broker
        broker_df = pd.read_csv(self.path_dim_broker)
        self.df = pd.merge(self.df, broker_df, on='broker_name', how='left')

        # Hands-on dim_province
        province_df = pd.read_csv(self.path_dim_province)
        self.df = pd.merge(self.df, province_df, on='province', how='left')

        # Hands-on dim_house
        house_df = pd.read_csv(self.path_dim_house)
        self.df = pd.merge(self.df, house_df, on='id', how='left')
        
        # Hands-on price column
        self.df['price'] = self.df['price'].str.replace('[\$,+,K]', '', regex=True).astype(int)

        # Hands-on columns to int
        self.df['id'] = self.df['id'].astype(int)
        
        self.write_csv(self.df[['id','price','key_broker','key_province','key_house', 'status_type', 'status_text']], self.path_fact_post)

def transform_fact_post():
    df = Transform_Dim_Post(['id', 'broker_name',  'address', 'price', 'status_type', 'status_text'])
    df.do_transform()
