print("наявні конвертації валют: \n1. UAH --> USD \n2. USD --> UAH \n3. UAH --> EUR \n4. EUR --> UAH")

option = input("Виберіть опцію (1/2/3/4): ")

if option == "1":  # UAH --> USD
    uah = float(input("введіть суму в гривнях "))
    exchange = float(input("введіть курс обміну "))
    if uah > 0 and exchange > 0:
        usd = uah / exchange
        print(f"{usd} доларів")
    else:
        print("значення не може бути відємним або 0")
elif option == "2":  # USD --> UAH
    usd = float(input("Введіть суму в долорах: "))
    exchange = float(input("Введіть курс обміну: "))
    if usd > 0 and exchange > 0:
        uah = usd * exchange
        print(f"{uah} гривнів")
    else:
        print("значення не може бути відємним або 0")
elif option == "3":  # UAH --> EUR
    uah = float(input("введіть суму в гривнях: "))
    exchange = float(input("Введіть курс обміну: "))
    if uah > 0 and exchange > 0:
        eur = uah / exchange
        print(f"{eur} єврів")
    else:
        print("значення не може бути відємним або 0")
elif option == "4":  # EUR --> UAH
    eur = float(input("Введіть суму в євро "))
    exchange = float(input("Введіть курс обміну: "))
    if eur > 0 and exchange > 0:
        uah = eur * exchange
        print(f"{uah} гривнів")
    else:
        print("значення не може бути відємним або 0")
else:
    print("опція відсутня")
