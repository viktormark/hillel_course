# Напишіть функцію square,
# яка приймає 1 аргумент,сторону квадрата,
# і повертає 3 значення (за допомогою кортежу):
# периметр квадрата, площа квадрата та діагональ квадрата.

def square(a):
    perimeter = a * 4
    area = a**2
    diagonal = a * (2**0.5)
    result = (perimeter, area, diagonal)
    return result


print(square(5))
