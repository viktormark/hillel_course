#Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа від значення start до величини end включно.
# Якщо користувач задасть перше число більше, ніж друге, просто поміняйте їх місцями.

def sum_range(start, end):
    if start > end:
        result = (start + end) * (start - end + 1) // 2
        return result
    else:
        result = (start + end) * (end - start + 1) // 2
        return result


print(sum_range(3,17))