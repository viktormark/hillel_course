#Напишіть функцію change_list,
# яка приймає список і змінює місця його перший і останній елемент.
# У вихідному списку щонайменше 2 елементи.

def change_list(l):
    if len(l) >= 2:
        result = []
        result.append(l[-1])
        middle = []
        middle.append(l[1:-1])
        for i in middle:
            for j in i:
                result.append(j)
        result.append(l[0])
        return result
    else:
        print("should be more then 2")


#print(change_list([1, 2, 3, 4, 5]))
# print(change_list([1,2,3,4,5,8,4,0]))
# print(change_list(["1","2","3","4","5"]))


