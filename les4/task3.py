# У вас є список змінних у форматі CamelCase ["FirstItem", "FriendsList", "MyTuple"] ,
# перетворити його у список змінних для Пайтона snace_case, "friends_list", "my_tuple"]

Camel = ["FirstItem", "FriendsList", "MyTuple"]
final = []
for i in Camel:
    my_list = list(i)
    my_list[0] = my_list[0].lower()
    part1 = []
    part2 = []
    snake = []
    for j in my_list:
        if j == j.upper():
            part1 = my_list[:my_list.index(j)]
            part1.append("_")
            #print(f"part1 {part1}")
            part2 = my_list[my_list.index(j):]
            for b in part2:
                if b == b.upper():
                    part2[part2.index(b)] = b.lower()
            #print(f"part2 {part2}")
            snake = part1 + part2
            #print(f"snake {snake}")
            result = "".join(snake)
            final.append(result)
print(final)


