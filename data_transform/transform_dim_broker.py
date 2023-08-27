from data_transform.transform import Transform

class Transform_Dim_Broker(Transform):
    def __init__(self, keep_columns):
        super().__init__(keep_columns)
    
    def do_transform(self):
        self.cleaning('id')
        self.reduplicate('id')

        # Replace empty value
        self.df['broker_name'] = self.df['broker_name'].fillna("Zillow")
        broker_df = self.df.groupby('broker_name').size().reset_index(name='count')

        # Generate ID
        broker_df['key_broker'] = broker_df.index + 1
        broker_df = broker_df[['key_broker', 'broker_name']]
        
        self.write_csv(broker_df, self.path_dim_broker)

def transform_dim_broker():
    df = Transform_Dim_Broker(['id', 'broker_name'])
    df.do_transform()