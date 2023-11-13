input_line = input().split(" ")
first = input_line[0]
second = input_line[1]

len_first_word = len(input_line[0])
len_second_word = len(input_line[1])

min_len = min(len_first_word, len_second_word)
sum_total = 0
for i in range(0, min_len):
    first_char_value = ord(first[i])
    second_char_value = ord(second[i])
    sum_total += first_char_value * second_char_value
if len_first_word > len_second_word:
    for i in range(min_len, len_first_word):
        first_char_value = ord(first[i])
        sum_total += first_char_value
elif len_second_word > len_first_word:
    for i in range(min_len, len_second_word):
        second_char_value = ord(second[i])
        sum_total += second_char_value

print(sum_total)