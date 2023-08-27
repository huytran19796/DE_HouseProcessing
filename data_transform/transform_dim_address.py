from data_transform.transform import Transform
import pandas as pd

class Transform_Dim_Address(Transform):
    def __init__(self, keep_columns):
        super().__init__(keep_columns)
    
    def do_transform(self):
        self.cleaning('id')
        self.reduplicate('id')
        self.df[['number-street', 'province', 'zipcode']] = self.df['address'].str.split(',', expand=True)

        # Hands-on province
        province_df = self.df.groupby('province').size().reset_index(name='count')
        province_df['key_province'] = province_df.index + 1
        province_df = province_df[['key_province', 'province']]
        self.write_csv(province_df, self.path_dim_province)

        # Hands-on detail street
        street_detail_df = self.df.groupby('number-street')['province'].first().reset_index(name='province')
        street_detail_df['key_dstreet'] = street_detail_df.index + 1

        street_detail_df = pd.merge(street_detail_df, province_df, on='province', how='inner')
        self.write_csv(street_detail_df[['key_dstreet','number-street', 'key_province']], self.path_dim_dstreet)

def transform_dim_address():
    df = Transform_Dim_Address(['id', 'address'])
    df.do_transform()