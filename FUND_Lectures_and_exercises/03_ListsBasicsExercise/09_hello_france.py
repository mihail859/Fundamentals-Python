#{type->price|type->price|type->price……|type->price}
#{budget}

train_ticket = 150
items_collection = input().split("|")
budget = float(input())

prices_after_selling = []
profit = 0

for items in items_collection:
    split_info = items.split("->")
    type_item = split_info[0]
    price = float(split_info[1])
    if type_item == "Clothes":
        if price > 50:
            continue
        if budget - price >= 0:
            budget -= price
            new_price = price * 1.40
            prices_after_selling.append(f"{new_price:.2f}")
            profit += float(f"{new_price:.2f}") - price

    elif type_item == "Shoes":
        if price > 35:
            continue
        if budget - price >= 0:
            budget -= price
            new_price = price * 1.40
            prices_after_selling.append(f"{new_price:.2f}")
            profit += float(f"{new_price:.2f}") - price

    elif type_item == "Accessories":
        if price > 20.50:
            continue
        if budget - price >= 0:
            budget -= price
            new_price = price * 1.40
            prices_after_selling.append(f"{new_price:.2f}")
            profit += float(f"{new_price:.2f}") - price

prices_after_selling = [str(p) for p in prices_after_selling]
print(" ".join(prices_after_selling))
print(f"Profit: {profit:.2f}")

prices_after_selling = [float(p) for p in prices_after_selling]
if sum(prices_after_selling) + budget >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")