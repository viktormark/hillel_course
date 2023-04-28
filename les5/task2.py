# Створити реалізацію квадратного рівняння a•x²+b•x+c=0(користувач вводить a, b, c),
# якщо дискримінант від'ємний викликати виняток DiscriminantError і вивести відповідне повідомлення.


class DiscriminantError(Exception):
    pass

A = float(input("enter a: "))
B = float(input("enter b: "))
C = float(input("enter c: "))

D = B ** 2 - 4 * A * C
print(D)

if D < 0:
    raise DiscriminantError("рівняння не має розвязків")
elif D == 0:
    x = -B / (2 * A)
    print(f"Корінь рівняння: x = {x}")  # 1, 6, 9
else:
    x1 = (-B + (D ** 0.5)) / (2 * A)
    x2 = (-B - (D ** 0.5)) / (2 * A)
    print(f"Корені рівняння: x1 = {x1}, x2 = {x2}")
