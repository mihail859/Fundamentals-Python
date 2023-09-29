cards = input().split(" ")
shuffle = int(input())
for _ in range(shuffle):
    final_deck = []
    middle = len(cards) // 2
    left_part = cards[:middle]
    right_part = cards[middle:]

    for i in range(len(left_part)):
        final_deck.append(left_part[i])
        final_deck.append(right_part[i])
    cards = final_deck

print(cards)