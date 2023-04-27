
my_word = input("enter your string: ")

my_list = my_word.split()

if len(my_list) < 3:
    print(f"кількість елементів менша за 3,\nпоточна кількість елементів = {len(my_list)}")
else:
    last_three = my_list[-3:]
    print(f"Останні три елементи зі списку: {last_three}")

