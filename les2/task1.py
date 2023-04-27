celsius = input("Введіть температуру в Цельсіях:")

if celsius.isalpha():

    print("введіть число")
else:

    celsius = float(celsius)
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.16
    print(f"Фаренгейт: {fahrenheit} \nКельвін: {kelvin}")
