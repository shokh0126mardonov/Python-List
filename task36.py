words = input('enter your words : ').split(',')

words = [word.strip() for word in words]

max_length = words[0]

for word in words[1:]:
    if len(word) > len(max_length):
        max_length = word

print(f"Eng uzun so'z bu {max_length}")