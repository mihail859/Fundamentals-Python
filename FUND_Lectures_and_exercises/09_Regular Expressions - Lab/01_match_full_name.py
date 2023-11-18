import re
pattern = r"\b[A-Z][a-z]{2,}\s[A-Z][a-z]{2,}"
input_name = input()
result = re.findall(pattern, input_name)
print(" ".join(result))