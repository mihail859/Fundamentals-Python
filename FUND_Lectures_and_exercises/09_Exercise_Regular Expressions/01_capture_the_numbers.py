import re

line = input()
pattern = '\d+'
while line:
    result = re.findall(pattern, line)
    if result:
        print(" ".join(result), end=" ")
    line = input()
