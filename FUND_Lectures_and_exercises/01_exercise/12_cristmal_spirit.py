quantity_of_decorations = int(input())
days = int(input())

total_cost = 0
total_spirit = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        total_cost += (quantity_of_decorations*2)
        total_spirit += 5
    if day % 3 == 0:
        total_cost += (quantity_of_decorations * 5) + (quantity_of_decorations * 3)
        total_spirit += 3 + 10
    if day % 5 == 0:
        total_cost += (quantity_of_decorations * 15)
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += 23
    if day == days and day % 10 == 0:
        total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")