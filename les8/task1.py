# Написать свой тип данных для сложения и вычитания,
# сравнение комплексных чисел.
# А так же правильного отображение их в консоли(magic method __str__).


class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Complex(new_x, new_y)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Complex(new_x, new_y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        if self.y >= 0:
            operator = "+"
        else:
            operator = "-"
        return f"{self.x} {operator} {abs(self.y)}i"


num1 = Complex(2, 3)
num2 = Complex(2, 3)

suma = num1 + num2
print(f"Сумма: {suma}")

sub = num1 - num2
print(f"вычитания: {sub}")

equal = num1 == num2
print(f"сравнение: {equal}")
#--