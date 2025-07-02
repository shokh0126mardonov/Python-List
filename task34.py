my_list = [1,2,3,7,8,9]

result = []

i = 0
while i < len(my_list):
    j = i + 1
    while j < len(my_list):
        if my_list[i] + my_list[j] == 10:
            result.append((my_list[i],my_list[j]))
        j+=1
    i+=1
            
print(result)