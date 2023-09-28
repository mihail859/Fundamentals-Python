n = int(input())
word = input()
all_words = []
filtered_words = []
for _ in range(n):
    string_word = input()
    all_words.append(string_word)
for i in range(n):
    current_word = all_words[i]
    if word in current_word:
        filtered_words.append(current_word)
print(all_words)
print(filtered_words)