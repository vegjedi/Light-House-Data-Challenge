import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('air_traffic_data.xlsx')

# condition Vancouver city, Groupby Origin City with Sum total of Passenger in the plane, then sort data in decending value
df_city=df[df.DEST_CITY_NAME == 'Vancouver, Canada'].groupby('ORIGIN_CITY_NAME')['PASSENGERS'].sum().sort_values(ascending=False)

print(df_city)

# select year 2021 and June month
df_2021_06=df[(df.YEAR == 2021) & (df.MONTH == 6)]

# draw histogram
plt.figure()
plt.hist(df_2021_06['DISTANCE'], bins = 8)
plt.show()
