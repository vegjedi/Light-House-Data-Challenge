landmarks = {
    "Big Ben": 12,
    "Tower Bridge": 25,
    "Buckingham Palace": 15,
    "Madame Tussauds": 25,
    "London Eye": 40,
    "Tower of London": 25,
    "Emirates Air Line cable car": 16,
    "London Transport Museum": 7,
    "Wembley Stadium": 8,
    "Hyde Park": 0,
    "The View from The Shard": 14
}

no=0

print('These are places that Dot may go:')

for place, time in landmarks.items():
    if time < 15:
        no += 1
        print(f'{no}. {place} - Waiting time is: {time} minute(s)')
