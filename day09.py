import pandas as pd
df = pd.read_excel('wine.xlsx')

print('No of wines with less than 13% alcohol are', len(df[df.Alcohol < 13]))

print('No of wines in class 3 are', len(df[df.Class == 3]))

print('No of wines with magnesim in between 90 and 100 are', len(df[df.Magnesium.between(90,100)]))

print('No of wines with magnesim higher than 90 and lower than 13.5% alcohol are', len(df[((df.Magnesium > 90) & (df.Alcohol < 13.5))]))
