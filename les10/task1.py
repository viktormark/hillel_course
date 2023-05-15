# Створити декоратор який вимірює час виконання функції
from datetime import datetime


def decorator(func):
    def wrapper(*args):
        start_time = datetime.now()
        res = func(*args)
        end_time = datetime.now()
        execution_time = end_time - start_time
        print("Час виконання: ", execution_time)
        return res

    return wrapper


@decorator
def hello(n):
    total = 0
    for i in range(n):
        total += i
    return total


hello(1000000)
