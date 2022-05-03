import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('toyota_cars.xlsx')

df_2020=df[df.Year == 2020].groupby('Category')['Category'].count()
plt.figure()
plt.bar(x = list(df_2020.index), height = list(df_2020))
plt.show()
