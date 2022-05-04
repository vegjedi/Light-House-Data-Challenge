import pandas as pd

df = pd.DataFrame([["Southern", "Southern","Southern","Southern"], 
                   ["Austria", "Australia", "New Zealand", "New Zealand"], 
                   ["Sydney", "Melbourne","Auckland","Wellington"],
                   [5.312, 5.078,1.463,0.215]],
                  index=['hemisphere','country', 'city','population'] 
                  ).transpose()

grouped = df.groupby(["hemisphere","country"])[["population"]].mean()

print(grouped.unstack(0))