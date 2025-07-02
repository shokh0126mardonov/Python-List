my_list = []

for i in range(1,6):
    var = input(f"{i} = ")
    my_list.append(var)
    
    
new_list = [] 
for i in my_list:
    if len(i)>5:
        new_list.append(i)
print(new_list)