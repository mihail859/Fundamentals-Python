tank_capacity = 255
new_tank = 0
n = int(input())
for i in range(n):
    litres_fill = int(input())
    if tank_capacity - litres_fill < 0:
        print("Insufficient capacity!")
        continue
    tank_capacity -= litres_fill
    new_tank += litres_fill

print(new_tank)