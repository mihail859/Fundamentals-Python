def first(dictionary, side, user):
    pass


def second(dictionary, user, side):
    pass


force_dict = dict()
while True:
    input_line = input()
    if input_line == 'Lumpawaroo':
        break
    if "|" in input_line:
        #/*"{force_side} | {force_user}"*/
        split_line = input_line.split(" | ")
        force_side = split_line[0]
        force_user = split_line[1]
        force_dict = first(force_dict, force_side, force_user)
    elif "->" in input_line:
        pass
