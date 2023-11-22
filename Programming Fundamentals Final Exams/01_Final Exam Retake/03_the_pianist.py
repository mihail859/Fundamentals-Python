def add(dictionary, piece_name, composer_name, key_sign):
    if piece_name in dictionary.keys():
        print(f"{piece_name} is already in the collection!")
        return dictionary
    dictionary[piece_name] = {"composer": composer_name, "key": key_sign}
    print(f"{piece_name} by {composer_name} in {key_sign} added to the collection!")
    return dictionary


def remove_piece(dictionary, piece_name):
    if piece_name in dictionary.keys():
        print(f"Successfully removed {piece_name}!")
        del dictionary[piece_name]
        return dictionary
    print(f"Invalid operation! {piece_name} does not exist in the collection.")
    return dictionary


def change_key(dictionary, piece_name, new_key_signature):
    if piece_name in dictionary.keys():
        dictionary[piece_name]["key"] = new_key_signature
        print(f"Changed the key of {piece_name} to {new_key_signature}!")
        return dictionary
    print(f"Invalid operation! {piece_name} does not exist in the collection.")
    return dictionary


number_of_pieces = int(input())
dictionary_pieces = dict()

for i in range(number_of_pieces):
    piece, composer, key = input().split("|")
    dictionary_pieces[piece] = {'composer': composer, 'key': key}

while True:
    command, *params = input().split("|")
    if command == 'Stop':
        break
    elif command == 'Add':
        new_piece = params[0]
        new_composer = params[1]
        new_key = params[2]
        dictionary_pieces = add(dictionary_pieces, new_piece, new_composer, new_key)

    elif command == 'Remove':
        piece_to_remove = params[0]
        dictionary_pieces = remove_piece(dictionary_pieces, piece_to_remove)

    elif command == 'ChangeKey':
        old_piece = params[0]
        new_key = params[1]
        dictionary_pieces = change_key(dictionary_pieces, old_piece, new_key)

for key_dict, value in dictionary_pieces.items():
    print(f"{key_dict} -> Composer: {value['composer']}, Key: {value['key']}")