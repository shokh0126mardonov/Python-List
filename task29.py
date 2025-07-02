my_list = []

for son in range(1,11):
    
    val = input(f"{son}-: ")
    my_list.append(val)


new_list = []

for i in my_list:
  if  my_list.count(i) == 1:
    new_list.append(i)

print(new_list)
    
