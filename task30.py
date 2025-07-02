my_list = []

for i in range(1,6):
    var = input(f"{i}-element = ")
    my_list.append(var)

new_list = []
for i in my_list:
   if  i[::-1] == i:
      new_list.append(i)

print(new_list) 