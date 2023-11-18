import re

pattern = r'\+359([\s|-])2\1[0-9]{3}\1[0-9]{4}\b'
numbers = input()
matches = re.finditer(pattern, numbers)

valid_numbers = []
for match in matches:
    valid_numbers.append(match.group(0))

print(", ".join(valid_numbers))