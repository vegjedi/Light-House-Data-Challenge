import pandas as pd

df = pd.read_excel('aus_weather.xlsx')

summer_winter=df[(df.season == 'summer')|(df.season == 'winter')] # sort summer and winter values only

short_table=summer_winter.groupby(['season','Location'])['Temp9am'].mean() # calculate the avg temp in Temp9am

un_table=short_table.unstack(0) # make unstack table with location, summer and winter columns

print((un_table['summer'] - un_table['winter']).head(3)) # show the top 3 cities by alphabet
