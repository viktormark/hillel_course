# Напишіть програму, яка виводить словник, в якому ключі є числами від 1 до 15 (обидва включені), а значення є квадратами ключів.
# Генерація ключів та значень має бути виконана через цикл.

result = {}

for key in range(1,16):
    result[key]= key**2

print(result)