import pandas as pd

df=pd.read_excel('dubai_properties_data.xlsx', index_col = 0)

property_price=df.groupby('neighborhood').agg(price_min=('price','mean'),price_max=('price','max')) # create df with min and max columns

print((property_price['price_max'] - property_price['price_min']).sort_values(ascending=False).head(1)) # sort value max - min and take first row
