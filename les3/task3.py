my_word = input("enter your string: ")
if my_word.startswith("abc"):
    my_word = my_word.replace("abc", "www", 1)
else:
    my_word = my_word + "zzz"

print(my_word)
