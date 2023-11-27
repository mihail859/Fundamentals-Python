def take_odd(line):
    new_line = [line[idx] for idx in range(len(line)) if idx % 2 != 0]
    return "".join(new_line)


def cut_function(line, idx, len_line):
    pass


input_line = input()
while True:
    command, *params = input().split()
    if command == 'TakeOdd':
        input_line = take_odd(input_line)
        print(input_line)

    elif command == 'Cut':
        index = int(params[0])
        length = int(params[1])
