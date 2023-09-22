import re


def check_valid_destination(input_destinations):
    destinations_list = []
    travel_points = 0

    pattern = r"(\=|\/)(?P<country>[A-Z][a-zA-Z]{2,})\1"
    result = re.finditer(pattern, input_destinations)
    for destination_valid in result:
        destination_valid = destination_valid.group("country")
        destinations_list.append(destination_valid)
        travel_points += len(destination_valid)
    print(f"Destinations: {', '.join(destinations_list)}\nTravel Points: {travel_points}")


data = input()
check_valid_destination(data)
