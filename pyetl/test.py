# empty string "", 0 -> Flase
result = -1

if result:
    print("exist")
else:
    print("empty")

printed_string = "exist" if result else "empty"
print(printed_string)

tmp_list = [1, 2, 3, 4, 5]

new_list = []
for i in tmp_list:
    if i > 3:
        new_list.append(i * 2)

print(new_list)

new_list = [i * 2 for i in tmp_list if i > 3]
print(new_list)
