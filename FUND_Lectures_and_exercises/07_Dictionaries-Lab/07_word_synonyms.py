n = int(input())
n *= 2
synonyms_dict = {}
for i in range(0, n, 2):
    word = input()
    synonym = input()
    if word not  in synonyms_dict.keys():
        synonyms_dict[word] = [synonym]
    else:
        synonyms_dict[word].append(synonym)

for key, value in synonyms_dict.items():
    print(f"{key} - {', '.join(value)}")