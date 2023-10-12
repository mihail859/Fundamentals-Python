def chars_in_range(char1, char2):
    chars_between = []
    for i in range(ord(char1) + 1, ord(char2)):
        chars_between.append(chr(i))
    return chars_between


first_char = input()
second_char = input()
print(' '.join(chars_in_range(first_char, second_char)))
