import pandas as pd

df=pd.read_excel('dubai_properties_data.xlsx', index_col = 0)

mean=df.groupby('neighborhood')[['price','size_in_sqft']].mean()

print(mean.sort_values('price',ascending=False).head(1)) # highest average price

print(mean.sort_values('size_in_sqft',ascending=False).head(1)) # highest average size
