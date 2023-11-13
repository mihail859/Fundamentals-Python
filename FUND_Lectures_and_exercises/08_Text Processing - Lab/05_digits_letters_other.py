input_line = input()
digits = []
letters = []
chars = []

for ch in input_line:
    if ch.isdigit():
        digits.append(ch)
    elif ch.isalpha():
        letters.append(ch)
    else:
        chars.append(ch)
print("".join(digits))
print("".join(letters))
print("".join(chars))