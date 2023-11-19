import re

pattern = '_[A-Za-z0-9]+'
data = input()

result = re.findall(pattern, data)
result_list = [word[1:] for word in result]
print(",".join(result_list))