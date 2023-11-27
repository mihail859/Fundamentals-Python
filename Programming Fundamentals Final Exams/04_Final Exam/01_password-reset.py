def take_odd(line):
    new_line = [line[idx] for idx in range(len(line)) if idx % 2 != 0]
    return "".join(new_line)


def cut_function(line, idx, len_line):
    substring = line[idx:idx + len_line]
    line = line.replace(substring, '')
    return line


def substitute(line, substring, replacement):
    if substring not in line:
        print("Nothing to replace!")
    else:
        line = line.replace(substring, replacement)
        print(line)
    return line


input_line = input()
while True:
    command, *params = input().split()
    if command == 'TakeOdd':
        input_line = take_odd(input_line)
        print(input_line)

    elif command == 'Cut':
        index = int(params[0])
        length = int(params[1])
        input_line = cut_function(input_line, index, length)
        print(input_line)

    elif command == 'Substitute':
        substr = params[0]
        substitute = params[1]
