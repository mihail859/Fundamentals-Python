input_line = input().split()
dictionary = {}

for i in range(0, len(input_line), 2):
    key = input_line[i]
    value = input_line[i + 1]
    dictionary[key] = int(value)

print(dictionary)
