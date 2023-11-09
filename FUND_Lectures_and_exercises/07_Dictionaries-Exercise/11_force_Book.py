def first(dictionary, side, user):
    for i in dictionary.values():
        if user in i:
            return dictionary
    if side not in dictionary.keys():
        dictionary[side] = [user]
    else:
        dictionary[side].append(user)
    return dictionary


def second(dictionary, user, side):
    for key, value in dictionary.items():
        if user in value:
            dictionary[key].pop(value.index(user))

    if side not in dictionary.keys():
        dictionary[side] = [user]
    else:
        dictionary[side].append(user)
    print(f"{user} joins the {side} side!")
    return dictionary


force_dict = dict()
while True:
    input_line = input()
    if input_line == 'Lumpawaroo':
        break
    if "|" in input_line:
        # /*"{force_side} | {force_user}"*/
        split_line = input_line.split(" | ")
        force_side = split_line[0]
        force_user = split_line[1]
        force_dict = first(force_dict, force_side, force_user)
    elif "->" in input_line:
        # a "force_user -> force_side"
        split_line = input_line.split(" -> ")
        force_user = split_line[0]
        force_side = split_line[1]
        force_dict = second(force_dict, force_user, force_side)

for key, value in force_dict.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for u in value:
            print(f"! {u}")