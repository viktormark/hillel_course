import json

with open("manager_sales.json") as l:
    templates = json.load(l)

f_name = ""
l_name = ""
res = 0

for i in templates:
    for j in i["cars"]:
        if len(i["cars"]) > res:
            res = len(i["cars"])
            f_name = i["manager"]["first_name"]
            l_name = i["manager"]["last_name"]

print(f"{f_name} {l_name} sold the most cars: {res}  ")
