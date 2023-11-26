import re

input_line = input()
pattern = r'(@|#)(?P<word1>[A-Za-z]{3,})\1{2}(?P<word2>[A-Za-z]{3,})\1'

result = re.finditer(pattern, input_line)

word_pairs = 0
mirror_words = []

for match in result:
    word1 = match.group('word1')
    word2 = match.group('word2')
    word_pairs += 1

    if word1 == word2[::-1]:
        mirror_words.append(f"{word1} <=> {word2}")

if word_pairs == 0:
    print("No word pairs found!")
    print("No mirror words!")

else:
    print(f"{word_pairs} word pairs found!")
    if mirror_words:
        print("The mirror words are:")
        print(", ".join(mirror_words))
    else:
        print("No mirror words!")