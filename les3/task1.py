my_word = input("enter your word: ")
my_word = my_word.replace(" ", "")
if my_word.isalpha():

    my_word = my_word.lower()
    reverse_word = my_word[::-1]

    if reverse_word == my_word:
        print("+")
    else:
        print("-")

else:
    print("enter only words")
