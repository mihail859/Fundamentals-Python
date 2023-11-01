products_dict = dict()
while True:
    command, *params = input().split(": ")
    if command == "statistics":
        break
    product = command
    quantity = int(params[0])
    if product in products_dict.keys():
        products_dict[product] += quantity
    else:
        products_dict[product] = quantity

print("Products in stock:")
for key, value in products_dict.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products_dict)}")
sum_of_values = lambda d: sum(d.values())
print(f"Total Quantity: {sum_of_values(products_dict)}")
