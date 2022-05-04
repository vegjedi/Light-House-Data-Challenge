import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('thai_tourism.xlsx')

for first_para in ('Number of tourists (m)', 'Receipts (bn $)'):
    for second_para in ('Receipts (bn $)', '% of GNP'):
        if first_para != second_para:
            print('Correlation between',first_para, 'and', second_para, 'is', round(df[[first_para, second_para]].corr().iloc[0,1],3))
            plt.figure()
            plt.scatter(x = df[first_para], y = df[second_para])
            plt.show()
