def add_stop_function(raw_info, idx, new_destination):
    if idx in range(0, len(raw_info)):
        before = raw_info[:idx]
        after = raw_info[idx:]
        raw_info = before + new_destination + after
    print(raw_info)
    return raw_info


def remove_stop(raw_info, starting_idx, ending_idx):
    if starting_idx in range(0, len(raw_info)) and ending_idx in range(0, len(raw_info)):
        first_part = raw_info[:starting_idx]
        second_part = raw_info[ending_idx + 1:]
        raw_info = first_part + second_part
    print(raw_info)
    return raw_info


def switch_function(raw_info, old, new):
    if old in raw_info:
        raw_info = raw_info.replace(old, new)
    print(raw_info)
    return raw_info


string_with_stops = input()
while True:
    command, *params = input().split(":")
    if command == "Travel":
        break

    if command == "Add Stop":
        index = int(params[0])
        string_data = params[1]
        string_with_stops = add_stop_function(string_with_stops, index, string_data)

    elif command == "Remove Stop":
        start_index = int(params[0])
        end_index = int(params[1])
        string_with_stops = remove_stop(string_with_stops, start_index, end_index)

    elif command == "Switch":
        old_string = params[0]
        new_string = params[1]
        string_with_stops = switch_function(string_with_stops, old_string, new_string)
print("Ready for world tour! Planned stops: {}".format(string_with_stops))