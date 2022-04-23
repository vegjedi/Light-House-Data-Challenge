import pandas as pd
df = pd.read_excel('aus_weather.xlsx')

df_date=df.set_index('Date') # set index to Date column

print(df_date[df_date.Location == 'Melbourne'].Temp9am.plot(kind='hist')) # draw plot histogram for Melbourne Temp9am

print(df_date[df_date.Location == 'Melbourne'].Rainfall.plot(kind='box')) # draw plot box for Melbourne Rainfall
