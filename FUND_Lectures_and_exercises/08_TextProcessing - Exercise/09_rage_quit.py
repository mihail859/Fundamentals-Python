command = input().upper()

current_message = ""
iterations = ""
final_message = ""

for index in range(len(command)):
    if not command[index].isdigit():
        current_message += command[index]
    else:
        for idx in range(index, len(command)):
            if command[idx].isdigit():
                iterations += command[idx]
            else:
                break
        final_message += current_message * int(iterations)
        current_message = ""
        iterations = ""

print(f"Unique symbols used: {len(set(final_message))}")
print(final_message)