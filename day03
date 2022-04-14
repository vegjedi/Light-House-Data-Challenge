import copy
layout = [
    ["O","e","e",None, "e","o","e",None, "o","o","E"], # row 1
    ["O","o","e",None, "e","o","e",None, "e","o","E"], # row 2
    ["O","o","o",None, "o","o","e",None, "o","e","O"], # row 3
    ["E","o","e",None, "e","o","e",None, "o","e","E"], # row 4 
    ["E","e","o",None, "e","e","e",None, "o","o","E"], # row 5
    ["O","e","e",None, "e","e","e",None, "e","e","E"]  # row 6
]

newlayout=layout.copy()

for x in range (len(layout)):
    for y in [0, -1]:
        if y == 0 and layout[x][y]=='E' and layout[x][y+1]=='e':
            print(x,y)
            break
        elif layout[x][y]=='E' and layout[x][y-1]=='e':
            print(x,y)
            break
    else:
        continue
    break

newlayout[x][y]='O'
print(newlayout)
