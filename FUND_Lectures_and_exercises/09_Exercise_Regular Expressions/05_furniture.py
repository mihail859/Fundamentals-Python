import re

pattern = r'>>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+\.?\d*)!(?P<quantity>\d+)'
total_price = 0
bought_furniture = []

line = input()
while line != "Purchase":
    result = re.match(pattern, line)

    if result:
        furniture = result.group("furniture")
        price = float(result.group("price"))
        quantity = int(result.group("quantity"))

        bought_furniture.append(furniture)
        total_price += price * quantity

    line = input()

print(bought_furniture)
print(total_price)