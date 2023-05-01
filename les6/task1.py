import math


def check_power_of_two(n):
    log2 = math.log2(n)
    if log2 == int(log2):
        print("Yes")
    else:
        print("No")


#check_power_of_two(8)


# 1. Дано натуральне число N. Виведіть слово YES, якщо число N є точним ступенем двійки,
# або слово NO інакше.
# 8 - YES, 3 - NO
