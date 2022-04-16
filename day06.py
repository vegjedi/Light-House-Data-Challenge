insert_spots=['w','n','n','w','N','n','w','N','N','w','n','n','w','n','n','W','W','W','W','n','n','w','n','n']

insert_type='wide'

def find_the_gates(spots,plane_type):
    for gate, gate_condition in enumerate(spots):
        if 'W'==plane_type[0].upper()==gate_condition:
            return gate
            break
        elif 'N'==plane_type[0].upper() and (gate_condition in ['N','W']):
            return gate
            break
    else:
        return 'No gate available for now'

print(find_the_gates(insert_spots,insert_type))
