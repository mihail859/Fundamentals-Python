new_message_list = []
secret_message = input().split()

for i in range(len(secret_message)):
    current_message = secret_message[i]
    chr_code = ""
    other_letters = ''
    for j in range(len(current_message)):
        if current_message[j].isdigit():
            chr_code += current_message[j]
        else:
            other_letters += current_message[j]

    if len(other_letters) > 1:
        new_word = chr(int(chr_code)) + other_letters[-1] + other_letters[1:-1] + other_letters[0]
    else:
        new_word = chr(int(chr_code)) + other_letters
    new_message_list.append(new_word)


print(" ".join(new_message_list))
