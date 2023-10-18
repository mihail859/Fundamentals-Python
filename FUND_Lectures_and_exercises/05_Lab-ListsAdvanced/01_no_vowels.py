vowels_list = ['a', 'o', 'u', 'e', 'i']
word_as_list = [w for w in input() if w.lower() not in vowels_list]
print(''.join(word_as_list))