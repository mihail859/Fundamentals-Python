import re

pattern = r'\b_[A-Za-z0-9]+\b'
data = input()

result = re.findall(pattern, data)
result_list = [word[1:] for word in result]
print(",".join(result_list))