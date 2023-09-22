def add_piece_func(pieces_data, piece_info, composer_info, key_info):
    if piece_info in pieces_data:
        print(f"{piece_info} is already in the collection!")
        return pieces_data
    pieces_data[piece_info] = [composer_info, key_info]
    print(f"{piece_info} by {composer_info} in {key_info} added to the collection!")
    return pieces_data


def remove_piece_func(pieces_data, remove_piece):
    if remove_piece in pieces_data.keys():
        del pieces_data[remove_piece]
        print(f"Successfully removed {remove_piece}!")
        return pieces_data
    print(f"Invalid operation! {remove_piece} does not exist in the collection.")
    return pieces_data


def change_key_func(pieces_data, pieces_to_change_key, new_key_to_the_piece):
    if pieces_to_change_key in pieces_data.keys():
        pieces_data[pieces_to_change_key][1] = new_key_to_the_piece
        print(f"Changed the key of {pieces_to_change_key} to {new_key_to_the_piece}!")
        return pieces_data
    print(f"Invalid operation! {pieces_to_change_key} does not exist in the collection.")
    return pieces_data


pieces_dictionary = {}
number_of_pieces = int(input())
for current_piece in range(number_of_pieces):
    piece_composer_key = input().split("|")
    piece, composer, key = piece_composer_key
    pieces_dictionary[piece] = [composer, key]

while True:
    command, *params = input().split("|")
    if command == "Stop":
        break
    if command == "Add":
        piece1, composer1, key1 = params
        pieces_dictionary = add_piece_func(pieces_dictionary, piece1, composer1, key1)

    elif command == "Remove":
        piece_to_remove = params[0]
        pieces_dictionary = remove_piece_func(pieces_dictionary, piece_to_remove)

    elif command == "ChangeKey":
        curr_piece, new_key = params
        pieces_dictionary = change_key_func(pieces_dictionary, curr_piece, new_key)

for final_piece, value in pieces_dictionary.items():
    final_composer = value[0]
    final_key = value[1]
    print(f"{final_piece} -> Composer: {final_composer}, Key: {final_key}")
