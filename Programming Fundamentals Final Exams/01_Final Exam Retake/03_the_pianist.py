number_of_pieces = int(input())
dictionary_pieces = dict()
for i in range(number_of_pieces):
    piece, composer, key = input().split("|")
    dictionary_pieces[piece] = {'composer': composer, 'key': key}
print(dictionary_pieces)