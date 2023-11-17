def check(current_ticket):
    symbols = ['@', '#', '$', '^']
    if not len(current_ticket) == 20:
        return "invalid ticket"
    left_part = current_ticket[0:10]
    right_part = current_ticket[10:]
    for match in symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbols_repetition = match * uninterrupted_match_length
            if winning_symbols_repetition in left_part and winning_symbols_repetition in right_part:
                if uninterrupted_match_length == 10:
                    return f'ticket "{current_ticket}" - {uninterrupted_match_length}{match} Jackpot!'
                return f'ticket "{current_ticket}" - {uninterrupted_match_length}{match}'

    return f'ticket "{current_ticket}" - no match'


lottery_tickets = input().split(", ")
for ticket in lottery_tickets:
    print(check(ticket))
