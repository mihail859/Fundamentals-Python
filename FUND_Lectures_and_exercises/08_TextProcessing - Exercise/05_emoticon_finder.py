# import re
#
# text_input = input()
# pattern = r':\S'
#
# result = re.findall(pattern, text_input)
# print("\n".join(result))

text_input = input()
for i in range(0, len(text_input)):
    if text_input[i] == ":":
        print(f":{text_input[i+1]}")
