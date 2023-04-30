# Напишіть функцію is_prime, яка приймає 1 аргумент - число від 2 до 1000,
# і повертає True, якщо це просте число, і False в іншому випадку.

import random


# тест Ферма

def fermat(p):

    if p < 2 or p > 1000:
        return False
    if p in [2, 3, 5, 7]:
        return True

    for i in range(5):
        a = random.randint(2, p - 2)
        if pow(a, p - 1, p) != 1: #a^(p-1) ≡ 1 (mod p)
            return False

    return True


# print(fermat(2))
# print(fermat(7))
print(fermat(47))
# print("--")
# print(fermat(4))
# print(fermat(10))
# print(fermat(20))
