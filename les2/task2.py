v1 = float(input("введіть v1: "))
v2 = float(input("введіть v2: "))
t1 = float(input("введіть t1: "))
t2 = float(input("введіть t2: "))

if v1 > 0 and v2 > 0 and t1 > 0 and t2 > 0:
    v3 = v2 + v1
    t3 = (v1 * t1 + v2 * t2) / v3
    print(f"об'єм суміші: {v3} \nтемпература суміші: {t3}")
else:
    print("значення не може бути відємним або 0")
