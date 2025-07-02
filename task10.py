list = [1,2,3,4,5]


index = int(input("indexni kiriting = "))
new = input()

if 0 <= index < len(list):
    list[index] = new
    print(list)
else:
    print("siz xato index kiritdingiz")

