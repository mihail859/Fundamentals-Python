dictionary_notes = {}
while True:
    command = input()
    if command == "End":
        break

    split_command = command.split("-")
    importance = int(split_command[0])
    value = split_command[1]
    dictionary_notes[importance] = value


sorted_dict = dict(sorted(dictionary_notes.items(), key=lambda item: item[0]))
print(list(sorted_dict.values()))

