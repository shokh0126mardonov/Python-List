list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Uzunligini tekshiramiz
if len(list1) != len(list2):
    print("Ro'yxat uzunligi teng emas")
else:
    for i in range(len(list1)):
        list1[i],list2[i] = list2[i],list1[i]
    print("list1:", list1)
    print("list2:", list2)
