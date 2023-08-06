def encrypted_function(message):

    while True:
        line = input()

        if line.startswith("Reveal"):
            print(f"You have a new text message: {message}")
            break
        line_command, *params = line.split(":|:")
        if line_command == "InsertSpace":
            idx = int(params[0])
            message = message[:idx] + " " + message[idx:]
            print(message)

        elif line_command == "Reverse":
            substring = params[0]
            if substring in message:
                message = message.replace(substring, "", 1)
                message = message + substring[::-1]
                print(message)
            else:
                print("error")

        elif line_command == "ChangeAll":
            substring = params[0]
            replacement = params[1]
            message = message.replace(substring, replacement)
            print(message)


command = input()
encrypted_function(command)
