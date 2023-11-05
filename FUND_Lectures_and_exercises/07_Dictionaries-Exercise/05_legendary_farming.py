farming_items = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

is_obtained = False
while True:
    input_data = input().split()
    for i in range(len(input_data), 2):
        quantity = int(input_data[i])
        material = input_data[i + 1].lower()
        if material not in farming_items.keys():
            farming_items[material] = 0
        farming_items[material] += quantity
        if farming_items["shards"] >= 250:
            is_obtained = True
            print("Shadowmourne obtained!")
            for key, value in farming_items.keys():
                if key != "shards":
                    print(f"{key}: {value}")
            break
        if farming_items["fragments"] >= 250:
            is_obtained = True
            print("Valanyr obtained!")
            for key, value in farming_items.keys():
                if key != "fragments":
                    print(f"{key}: {value}")
            break
        if    