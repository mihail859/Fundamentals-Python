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
    for key, value in dictionary.values():
        if user in value:
            dictionary[key].pop(value.index(user))
            return dictionary
    # if force_side not in force_side_dictionary.keys():
    #     force_side_dictionary[force_side] = [force_user]
    # else:
    #     force_side_dictionary[force_side].append(force_user)
    if side not in dictionary.keys():
        dictionary[side] = [user]
    else:
        dictionary[side].append(user)
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

