import json

max_female = 0
id_female = ""

with open("group_people.json") as l:
    templates = json.load(l)

for i in templates:
    count = 0
    for j in i['people']:
        if j['gender'] == 'Female':
            if j['year'] >= 1977:
                count += 1
    if count > max_female:
        max_female = count
        id_female = i['id_group']

print(f"{max_female} {id_female}")



