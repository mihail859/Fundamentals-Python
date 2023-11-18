import re
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
input_name = input()
result = re.findall(pattern, input_name)
print(" ".join(result))