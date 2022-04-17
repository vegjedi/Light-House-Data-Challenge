import pandas as pd
df = pd.read_excel('fc_barcelona.xlsx')

points = df.Pts
games_played = df.MP
wins = df.W
losses = df.L
attendance = df.Attendance.dropna() # skipping missing values (NaN)

q1=games_played.max()
q2=attendance.mean()
q3=wins.median() - losses.median()
q4=wins.min()
q5=points.max() - points.min()

print(q1, q2, q3, q4, q5)

print(df.style.hide_index())