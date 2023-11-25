def add_stop(stops, idx, stop):
    if idx in range(0, len(stops)):
        before = stops[:idx]
        after = stops[idx:]
        stops = before + stop + after
    return stops


def remove_stop(stops, start, end):
    if start in range(0, len(stops)) and end in range(0, len(stops)):
        before = stops[:start]
        after = stops[end + 1:]
        stops = before + after
    return stops


def switch_stops(stops, old, new):
    if old in stops:
        stops = stops.replace(old, new)
    return stops


input_string = input()
while True:
    command, *params = input().split(":")
    if command == "Travel":
        print(f"Ready for world tour! Planned stops: {input_string}")
        break
    elif command == "Add Stop":
        index = int(params[0])
        string = params[1]
        input_string = add_stop(input_string, index, string)
        print(input_string)

    elif command == "Remove Stop":
        start_index = int(params[0])
        end_index = int(params[1])
        input_string = remove_stop(input_string, start_index, end_index)
        print(input_string)

    elif command == "Switch":
        old_stop = params[0]
        new_stop = params[1]
        input_string = switch_stops(input_string, old_stop, new_stop)
        print(input_string)
