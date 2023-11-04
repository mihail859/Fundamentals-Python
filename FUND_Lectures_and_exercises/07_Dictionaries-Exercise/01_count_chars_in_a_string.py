text_input = input()
text_array = [w for w in text_input if w != ' ']
char_dict = {}
for char in text_array:
    if char not in char_dict.keys():
        char_dict[char] = 1
    else:
        char_dict[char] += 1

for key, value in char_dict.items():
    print(f"{key} -> {value}")