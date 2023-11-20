import re

input_line = input()
pattern = r'([a-z0-9]+[a-z0-9\.\-\_])@([a-z\-]+)([a-z0-9\.]+)\b'
result = re.finditer(pattern, input_line)
for match in result:
    print(match.group(0))