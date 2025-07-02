my_list = []

for i in range(1,8):
    var = input(f"{i} = ")
    my_list.append(var)
    
max_qiymat = 0
kop_qatnashgan = 0  

for i in my_list:
    s = my_list.count(i)
    if s > max_qiymat:
        max_qiymat = s
        kop_qatnashgan = i
        
print(f"{kop_qatnashgan} soni {max_qiymat} marta qatnashgan") 
