from sys import getsizeof

'''Malumot qo'shish 1) append oxiriga element qo'shish
2)extent([]) oxirida bir nechta element qo'shadigan metod
3)insert(index,value) xoxlagan indexni berib osha indexga ozimizni 
   ozgaruvchimizni taminlab qo'yamiz

'''

'''Malumotlarni o'chirish 1).remove(qiymat) ushbu remove ichidagi qiymatni listdan o'chirib tashlaydi
.pop(index) ushbu indexdagi qiymat o'chirib tashlanadi va buni biror o'zgaruvchiga tenglab foydalansan ham bo'ladi

'''

'''.reverse() ushbu esa listni teskari qilib beradi

'''

'''
.sort() esa bir turdagi malumotlarni tartiblab beradi
'''

list = [1,2,3,4,5]

list.insert(45,'olma')
print(list)