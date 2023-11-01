chars_input = input().split(", ")
dictionary = {chars_input[i]: ord(chars_input[i]) for i in range(len(chars_input))}
print(dictionary)