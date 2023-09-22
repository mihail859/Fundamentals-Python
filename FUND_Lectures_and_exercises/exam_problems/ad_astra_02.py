import re

pattern = r"(#|\|)(?P<item>[a-zA-Z\s]+)\1(?P<date>[\d]{2}/[\d]{2}/[\d]{2})\1(?P<cal>[\d]{1,5})\1"
input_data = input()

result = re.finditer(pattern, input_data)

total_calories = 0
items_list = []
days = 0

if result:
    for single_data in result:
        total_calories += int(single_data.group("cal"))

        a = f"Item: {single_data.group('item')}, Best before: {single_data.group('date')}, " \
            f"Nutrition: {single_data.group('cal')}"
        items_list.append(a)

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
if items_list:
    for i in items_list:
        print(i)