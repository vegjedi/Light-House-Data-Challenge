import pandas as pd
df = pd.read_excel('paris_landmarks.xlsx')

print(df.loc[df.price == df.price.max(),'landmark']) # most expensive place

print(df.queue_time.mean()) # average waiting time
