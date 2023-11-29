n = int(input())
heroes_dict = dict()

for _ in range(n):
    input_line = input().split()
    name = input_line[0]
    hit_points = int(input_line[1])
    mana_points = int(input_line[2])
    heroes_dict[name] = {'hp': hit_points, 'mp': mana_points}

print(heroes_dict)