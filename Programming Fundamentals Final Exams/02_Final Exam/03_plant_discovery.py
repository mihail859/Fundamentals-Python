def rate_plant(dictionary, name, value):
    if name not in dictionary.keys():
        print("error")
    else:
        dictionary[name]['rating'].append(value)
    return dictionary


def update_rarity(dictionary, name, new_rarity_plant):
    if name not in dictionary.keys():
        print("error")
    else:
        dictionary[name]['rarity'] = new_rarity_plant
    return dictionary


def reset_ratings(dictionary, name):
    if name not in dictionary.keys():
        print("error")
    else:
        dictionary[name]['rating'].clear()
    return dictionary


n = int(input())
plant_dict = {}
for _ in range(n):
    info = input().split("<->")
    plant = info[0]
    rarity = int(info[1])
    plant_dict[plant] = {'rarity': rarity, 'rating': []}

while True:
    command, *params = input().split(": ")
    if command == "Exhibition":
        break

    elif command == "Rate":
        split_data = params[0].split(" - ")
        plant_name = split_data[0]
        rating = int(split_data[1])
        plant_dict = rate_plant(plant_dict, plant_name, rating)

    elif command == "Update":
        split_data = params[0].split(" - ")
        plant_name = split_data[0]
        new_rarity = int(split_data[1])
        plant_dict = update_rarity(plant_dict, plant_name, new_rarity)

    elif command == "Reset":
        plant_name = params[0]
        plant_dict = reset_ratings(plant_dict, plant_name)

print("Plants for the exhibition:")
for key, value in plant_dict.items():
    rarity_value = value["rarity"]
    ratings_list = value["rating"]
    if ratings_list:
        avg_rating = sum(ratings_list) / len(ratings_list)
    else:
        avg_rating = 0.00
    print(f"- {key}; Rarity: {rarity_value}; Rating: {avg_rating:.2f}")
