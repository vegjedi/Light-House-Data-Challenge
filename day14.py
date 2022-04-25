import pandas as pd

df = pd.read_excel('nz_car_traffic.xlsx')

# region (using variable regionName) with the lowest total amount of light (using variable classWeight) traffic (12 - West Coast)
print(df[df.classWeight == 'Light'].groupby('regionName')['trafficCount'].sum().sort_values(ascending=True))

# region with the lowest total amount of heavy (using variable classWeight) traffic (12 - West Coast)
print(df[df.classWeight == 'Heavy'].groupby('regionName')['trafficCount'].sum().sort_values(ascending=True))

# a bar chart, which month had the lowest amount of total traffic in 2020 (April)
print(df.groupby('month')['trafficCount'].sum().plot.bar(x='month', y='trafficCount', rot=0))

# percent of New Zealand’s traffic (using variable trafficCount) was classified as heavy (4.3%)
sum_group=df.groupby('classWeight')['trafficCount'].sum().reset_index()
sum_group['percent']=100 * sum_group['trafficCount']/sum_group['trafficCount'].sum()
print(sum_group)
