def move(message, letters):
    sequence = message[:letters]
    second_part = message[letters:]
    new_message = second_part + sequence
    return new_message


def insert_func(message, idx, letters_sequence):
    part_before = message[:idx]
    part_after = message[idx:]
    new_message = part_before + letters_sequence + part_after
    return new_message


def change_all_func(message, old, new):
    pass


message_line = input()

while True:
    command, *params = input().split("|")
    if command == "Decode":
        break

    elif command == "Move":
        number_of_letters = int(params[0])
        message_line = move(message_line, number_of_letters)
        print(message_line)

    elif command == "Insert":
        index = int(params[0])
        value = params[1]
        message_line = insert_func(message_line, index, value)
        print(message_line)

    elif command == "ChangeAll":
        substring = params[0]
        replacement = params[1]
