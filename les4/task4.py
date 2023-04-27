# Створіть словник з чотирма назвами мов програмування (ключі) та іменами розробників цих мов (значення).
# Виведіть по черзі для усіх елементів словника повідомлення типу My favorite programming language is Python.
# It was created by Guido van Rossum..
# Видаліть, на ваш вибір, одну пару «мова: розробник» із словника. Виведіть словник на екран.

languages = {
    'Python': 'Guido van Rossum',
    'Java': 'James Gosling',
    'JavaScript': 'Brendan Eich',
    'C++': 'Bjarne Stroustrup\n'
}

for key, value in languages.items():

    print(f"My favorite programming language is {key} , It was created by {value} ")

del languages['JavaScript']
print(languages)
