text_input = input()
message = ""
last_symbol = ""
for ch in text_input:
    if ch != last_symbol:
        message += ch
        last_symbol = ch
print(message)