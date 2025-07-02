
new_list = []

while True:
    name = input('enter name : ')
    if name == '':
        break
    else:
        new_list.append(name)

print(len(new_list))