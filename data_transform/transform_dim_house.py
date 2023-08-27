from data_transform.transform import Transform

class Transform_Dim_House(Transform):
    def __init__(self, keep_columns):
        super().__init__(keep_columns)
    
    def do_transform(self):
        self.cleaning('id')
        self.reduplicate('id')
        
        # Generate ID
        self.df['id'] = self.df['id'].astype(int)
        self.df['key_house'] = self.df.index + 1

        # Replace empty value
        self.df['area'].fillna(0, inplace=True)
        self.df['beds'].fillna(0, inplace=True)
        self.df['baths'].fillna(0, inplace=True)
        self.df['beds'] = self.df['beds'].astype(int)
        self.df['baths'] = self.df['baths'].astype(int)

        self.write_csv(self.df, self.path_dim_house)

def transform_dim_house():
    df = Transform_Dim_House(['id', 'area', 'beds', 'baths', 'detail_url', 'image_urls'])
    df.do_transform()