def insert_space_func(message, idx):
    new_message = message[:idx] + " " + message[idx:]
    return new_message


def reverse_func(message, substr):
    if substr not in message:
        print("error")
    else:
        message = message.replace(substr, substr[::-1], 1)
        print(message)
    return message


def change_all_func(message, old, new):
    message = message.replace(old, new)
    return message


input_message = input()
while True:
    command, *params = input().split(":|:")
    if command == "Reveal":
        break
    elif command == "InsertSpace":
        index = int(params[0])
        input_message = insert_space_func(input_message, index)
        print(input_message)

    elif command == "Reverse":
        substring = params[0]
        input_message = reverse_func(input_message, substring)


    elif command == "ChangeAll":
        substring = params[0]
        replacement = params[1]
        input_message = change_all_func(input_message, substring, replacement)

        print(input_message)

print(f"You have a new text message: {input_message}")
