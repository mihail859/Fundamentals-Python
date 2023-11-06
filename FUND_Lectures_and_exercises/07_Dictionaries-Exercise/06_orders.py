def add_product(shopping_list, product, price, quantity):
    if product not in shopping_list.keys():
        shopping_list[product] = {"quantity1": 0, "price1": price}
    shopping_list[product]['quantity1'] += quantity
    shopping_list[product]['price1'] = price
    return shopping_list


def get_shopping_list(shopping_list):
    for key, value in shopping_list.items():
        print(f"{key} -> {(value['quantity1'] * value['price1']):.2f}")


shopping_list_dict = dict()
while True:
    command = input()
    if command == "buy":
        get_shopping_list(shopping_list_dict)
        break
    split_command = command.split()
    product_name = split_command[0]
    price_product = float(split_command[1])
    product_quantity = int(split_command[2])
    shopping_list_dict = \
        add_product(shopping_list_dict,
                    product_name,
                    price_product,
                    product_quantity)

