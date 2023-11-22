def add(dictionary, piece_name, composer_name, key_sign):
    if piece in dictionary.keys():
        print()


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
        pass

    elif command == 'ChangeKey':
        pass
