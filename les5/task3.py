"""Напишіть інтерактивний калькулятор. Передбачається, що користувач вводить формулу,
що складається з числа, оператора (як мінімум + і -) та іншого числа, розділених пробілом (наприклад, 1 + 1).
Використовуйте str.split()
a. Якщо вхідні дані не складаються з трьох елементів, генеруйте ексепшн FormulaError.
b. Спробуйте перетворити перший і третій елемент на float ( float_value = float(str_value)).
Спіймайте будь-яку ValueError і згенеруйте замість нього FormulaError
c. Якщо другий елемент не є «+» або «-» або «*» або «/», киньте Exception FormulaError"""
class FormulaError(Exception):
    pass


value = input("введіть формулу (наприклад, 1 + 1) : ")

my_list = value.split()

if len(my_list) < 3 or len(my_list) > 3:
    raise FormulaError("введіть правильний формат формули")

first_value, operator, second_value = my_list
try:
    first_value = float(first_value)
    second_value = float(second_value)
except ValueError:
    raise FormulaError("недійсне значення")

if operator == "+":
    res = float(first_value) + float(second_value)
    print(res)
elif operator == "-":
    res = float(first_value) - float(second_value)
    print(res)
elif operator == "*":
    res = float(first_value) * float(second_value)
    print(res)
elif operator == "/":
    res = float(first_value) / float(second_value)
    print(res)
else:
    raise FormulaError("Невірний оператор")



