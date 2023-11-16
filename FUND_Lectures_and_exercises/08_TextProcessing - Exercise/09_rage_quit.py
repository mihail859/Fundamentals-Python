string_input = input()
output = ''
pattern = ""
for i in range(len(string_input)):
    current_ch = string_input[i]
    if not current_ch.isdigit():
        pattern += current_ch
    if current_ch.isdigit() and string_input[i+1].isdigit():
        output += ""