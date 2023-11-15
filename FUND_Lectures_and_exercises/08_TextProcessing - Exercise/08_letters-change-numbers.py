input_line = input().split()

total_sum = 0

for sequence in input_line:
    current_sum = 0
    if sequence[0].isupper():
        letter_position = ord(sequence[0]) - 64
        number = int(sequence[1:-1])
        current_sum += number / letter_position
    if sequence[0].islower():
        letter_position = ord(sequence[0]) - 96
        number = int(sequence[1:-1])
        current_sum += number * letter_position
    if sequence[-1].isupper():
        letter_position = ord(sequence[0]) - 64
        number = int(sequence[1:-1])
        current_sum += number - letter_position
    if sequence[-1].islower():
        letter_position = ord(sequence[0]) - 96
        number = int(sequence[1:-1])
        current_sum += number * letter_position