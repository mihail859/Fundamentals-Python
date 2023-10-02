# Type of Fire	Range
# High	        81 - 125
# Medium	        51 - 80
# Low	            1 - 50
cells = input().split("#")
water = int(input())
effort = []
cells_stats = []

for cell in cells:
    split_data = cell.split(" = ")
    type_of_fire = split_data[0]
    amount = int(split_data[1])
    if type_of_fire == "High" and amount in range(81, 126):
        if water - amount >= 0:
            water -= amount
            e = 0.25 * amount
            effort.append(e)
            cells_stats.append(amount)
        else:
            continue
    elif type_of_fire == "Medium" and amount in range(51, 81):
        if water - amount >= 0:
            water -= amount
            e = 0.25 * amount
            effort.append(e)
            cells_stats.append(amount)
        else:
            continue
    elif type_of_fire == "Low" and amount in range(1, 51):
        if water - amount >= 0:
            water -= amount
            e = 0.25 * amount
            effort.append(e)
            cells_stats.append(amount)
        else:
            continue
print("Cells:")
for i in range(len(cells_stats)):
    print(f"- {cells_stats[i]}")
print(f"Effort: {sum(effort):.2f}")
print(f"Total Fire: {sum(cells_stats)}")