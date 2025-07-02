words = input('royxatni kiriting : ').split(',')

up_to_tree = []
up_to_six = []
grater_then_six = []

for word in words:
    length = len(word)
    if length <= 3:
        up_to_tree.append(word)
    elif 4 <= length <= 6:
        up_to_six.append(word)
    elif length > 6:
        grater_then_six.append(word)
        
print(f'3 ta gacha uzunlik {up_to_tree}')
print(f'3 dan 6 ta gacha uzunlik {up_to_six}')
print(f'6  tadan katta gacha uzunlik {grater_then_six}')
    