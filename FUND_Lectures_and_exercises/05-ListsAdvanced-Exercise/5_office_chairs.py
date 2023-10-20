number_of_rooms = int(input())
free_chairs = 0
is_ok = True
for room in range(1, number_of_rooms + 1):
    data = input().split()
    chairs = len(data[0])
    people = int(data[1])
    if chairs < people:
        print(f"{people - chairs} more chairs needed in room {room}")
        is_ok = False
    else:
        free_chairs += abs(people - chairs)

if is_ok:
    print(f"Game On, {free_chairs} free chairs left")