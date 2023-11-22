import re

pattern = r'(\||#)(?P<item>[a-zA-Z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d{1,5})\1'

foods_input = input()
result = re.finditer(pattern, foods_input)

sum_calories = 0
product_list = []
if result:

    for match in result:
        product = match.group('item')
        expiration_date = match.group('date')
        calories = int(match.group('calories'))
        sum_calories += calories
        a = f"Item: {product}, Best before: {expiration_date}, Nutrition: {calories}"
        product_list.append(a)


days = sum_calories // 2000
print(f"You have food to last you for: {days} days!")
if product_list:
    for i in product_list:
        print(i)
