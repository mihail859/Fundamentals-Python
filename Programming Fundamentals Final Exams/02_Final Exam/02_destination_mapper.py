import re

pattern = r'(=|\/)(?P<place>[A-Z]{1}[A-Za-z]{2,})\1'
input_data = input()

result = re.finditer(pattern, input_data)
destinations = []
tourist_points = 0
for match in result:
    country = match.group(2)
    tourist_points += len(country)
    destinations.append(country)
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {tourist_points}")