import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
conn = sqlite3.connect("world.db")

# select worldcities tables
worldcities=pd.read_sql('select * from worldcities',conn)

# remove all null value in population
df=worldcities[worldcities.population.notnull()]

# plot hist 
plt.figure()
plt.hist(df['population'],bins = 8)
plt.show()

# draw bar chart of the top 10 country with sum of population of all cities, which are sorted in decending order
df.groupby('country')['population'].sum().sort_values(ascending=False).head(10).plot(kind='bar',x='country')
