input_line = [word.lower() for word in input().split()]
occurrences_dict = dict()
for item in input_line:
    if item in occurrences_dict.keys():
        occurrences_dict[item] += 1
    else:
        occurrences_dict[item] = 1

answer = []
for key, value in occurrences_dict.items():
    if value % 2 != 0:
        answer.append(key)

print(" ".join(answer))