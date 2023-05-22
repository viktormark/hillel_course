# Використовуючи модуль argparse створити програму розрахунку квадратного рівняння.
# Запуск програми python main.py -a={} -b={} c={} де параметри (a, b, c - параметри квадратного рівняння),
# за замовчуванням параметр а = 0
# При виклику програми з прапорцем --help вивести інформацію про програму та про параметри
import argparse


class DiscriminantError(Exception):
    pass


def perform_operation(a, b, c):
    D = b ** 2 - 4 * a * c

    if D < 0:
        raise DiscriminantError("рівняння не має розвязків")
    elif D == 0:
        x = -b / (2 * a)
        print(f"Корінь рівняння: x = {x}")  # 1, 6, 9
    else:
        x1 = (-b + (D ** 0.5)) / (2 * a)
        x2 = (-b - (D ** 0.5)) / (2 * a)
        print(f"Корені рівняння: x1 = {x1}, x2 = {x2}")

def main():
    parser = argparse.ArgumentParser(description="Програма розрахунку квадратного рівняння")

    parser.add_argument('-a', type=float, help='Первое число', default=0)
    parser.add_argument('-b', type=float, help='Второе число')
    parser.add_argument('-c', type=float, help='третье число')

    args = parser.parse_args()

    perform_operation(args.a, args.b, args.c)

if __name__ == '__main__':
    main()

#python les12/task1.py --help
#python les12/task1.py -a=1 -b=6 -c=1