my_list = []

for i in range(1,6):
    var = input(f"{i} = ")
    my_list.append(var)

my_list1 = []
for i in range(1,5):
    var = input(f"{i} = ")
    my_list1.append(var)
   
my_list2 = []   
for i in my_list:
    for z in my_list1:
        if  i == z:
            my_list2.append(i)
            
print(my_list2)