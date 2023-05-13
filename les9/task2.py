# Знайти найуспішнішого менеджера за підсумковою сумою продажів.
# Як відповідь потрібно через пробыл вказати спершу його ім'я, потім прізвище і після загальну суму його продажів.Файл manager_sales.json

import json


with open("manager_sales.json") as l:
    templates = json.load(l)

manager = ""
result = 0

for i in templates:
    sales = 0
    f_name = i["manager"]["first_name"]
    l_name = i["manager"]["last_name"]

    for j in i["cars"]:
        sales = sales + j["price"]
    if sales > result:
        result = sales
        manager = f_name + " " + l_name


print(f"{manager}  {result}  ")




