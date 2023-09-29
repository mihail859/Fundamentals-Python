cards = input().split(" ")
count_iterations = int(input())
for _ in range(count_iterations):
    first_half = []
    second_half = []

# ace two three four five six
# 1
    for idx in range(1, len(cards) - 1):
        curr_card = cards[idx]
        if idx < len(cards) / 2:
            first_half.append(curr_card)
        else:
            second_half.append(curr_card)

    mixed_cards = []
    first_half_idx = 0
    second_half_idx = 0
    for i in range(len(first_half) * 2):
        if i % 2 == 0:

            mixed_cards.append(second_half[second_half_idx])
            second_half_idx += 1
        else:

            mixed_cards.append(first_half[first_half_idx])
            first_half_idx += 1

    cards = [cards[0]] + mixed_cards + [cards[-1]]
print(cards)