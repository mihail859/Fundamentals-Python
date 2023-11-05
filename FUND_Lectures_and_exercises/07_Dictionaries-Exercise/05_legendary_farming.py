farming_items = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
input_data = input().split()
is_obtained = False
while not is_obtained:

    for i in range(0, len(input_data), 2):
        quantity = int(input_data[i])
        material = input_data[i + 1].lower()
        if material not in farming_items.keys():
            farming_items[material] = 0
        farming_items[material] += quantity
        if farming_items["shards"] >= 250:
            farming_items["shards"] -= 250
            is_obtained = True
            print("Shadowmourne obtained!")
            for key, value in farming_items.items():
                print(f"{key}: {value}")
            break
        if farming_items["fragments"] >= 250:
            is_obtained = True
            farming_items["fragments"] -= 250
            print("Valanyr obtained!")
            for key, value in farming_items.items():
                print(f"{key}: {value}")
            break
        if farming_items["motes"] >= 250:
            is_obtained = True
            farming_items["motes"] -= 250
            print("Dragonwrath obtained!")
            for key, value in farming_items.items():
                print(f"{key}: {value}")
            break
    if is_obtained:
        break
    input_data = input().split()
