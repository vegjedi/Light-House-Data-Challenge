import pandas as pd
df = pd.read_excel('fc_barcelona.xlsx')

points = df.Pts
games_played = df.MP
wins = df.W
losses = df.L
attendance = df.Attendance.dropna() # skipping missing values (NaN)

q1=games_played.max() # maximum amount of games Barcelona playes in 1 season
q2=attendance.mean() # average attendance across the seasons
q3=wins.median() - losses.median() # difference between median value of wins and losses
q4=wins.min() # minimum number of games Barcelona managed to win in 1 season
q5=points.max() - points.min() # difference between max and min amount of points Barcelona was able to get in all seasons

print(q1, q2, q3, q4, q5)
