# Створити декоратор який кожен раз буде записувати у файл результат роботи якоїсь функції після її виклику
# (наприклад функція яка прораховує суму всіх переданих аргументів *args).
# Запис в файл формату ""Function launched at {час запуску} with result {результат роботи функції}
from datetime import datetime


def decorator2(func):
    def wrapper(*args):
        res = func(*args)
        start_time = datetime.now()
        file = open('result.txt', 'w')
        file.write(f"Function launched at {start_time} with result {res}")
        file.close()
        return res

    return wrapper


@decorator2
def suma(*args):
    return sum(args)


suma(5, 5, 5, 6)
