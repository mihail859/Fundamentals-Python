def out_of_stock(gifts_list, curr_gift):
    for i in range(len(gifts_list)):
        if gifts_list[i] == curr_gift:
            gifts_list[i] = "None"

    return gifts_list


def required(gifts_list, new_gift, idx):
    if idx in range(len(gifts_list)):
        gifts_list[idx] = new_gift

    return gifts_list


def just_in_case(gifts_list, new_gift):
    gifts_list[-1] = new_gift
    return gifts_list


gifts = [p for p in input().split()]
while True:
    command = input().split()
    if command[0] +" " + command[1] == "No Money":
        break
    elif command[0] == "OutOfStock":
        gift = command[1]
        gifts = out_of_stock(gifts, gift)
    elif command[0] == "Required":
        gift = command[1]
        index = int(command[2])
        gifts = required(gifts, gift, index)
    elif command[0] == "JustInCase":
        gift = command[1]
        gifts = just_in_case(gifts, gift)

list_final = [g for g in gifts if g != "None"]
print(" ".join(list_final))