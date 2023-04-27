first_value = float(input("введіть перше число: "))
second_value = float(input("введіть друге число: "))
znak = input("введіть оператор (+, -, *, /): ")


if znak == "+":
    res = first_value + second_value
    print(res)
elif znak == "-":
    res = first_value - second_value
    print(res)
elif znak == "*":
    res = first_value * second_value
    print(res)
elif znak == "/":
    res = first_value / second_value
    print(res)
else:
    print("некоректне значення")