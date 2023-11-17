lottery_tickets = input().split(", ")
for ticket in lottery_tickets:
    if not len(ticket) == 20:
        print("invalid ticket")
    else:
        print("valid ticket")