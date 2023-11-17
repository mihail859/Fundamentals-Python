def check(tickets, current_ticket):
    symbols = ['@', '#', '$', '^']
    if not len(current_ticket) == 20:
        return "invalid ticket"
    left_part = tickets[0:10]
    right_part = tickets[10:]
    for match in symbols:
        




lottery_tickets = input().split(", ")
for ticket in lottery_tickets:
    print(check(lottery_tickets, ticket))