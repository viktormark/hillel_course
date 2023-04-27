# Є список друзів ["John", "Marta", "James", "Amanda", "Marianna"].
# Виведіть імена в консолі,
# кожен з нового рядка, вирівнюючи праву сторону,
# використовуючи метод рядка та форматування через F String.
# Також над іменами першим рядком виведіть NAME,
# де NAME має бути посередині(string.center()), а решта простору заповнена символом "*"


my_list = ["john", "marta", "james", "amanda", "marianna"]
name = "NAME"
print(name.center(10, "*"))

for i in my_list:
    print(f"{i.capitalize().rjust(10)}")
