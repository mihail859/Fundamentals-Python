import re

input_line = input()
searched_word = input()
pattern = rf'\b{searched_word}\b'

result = re.findall(pattern, input_line, re.IGNORECASE)
print(len(result))