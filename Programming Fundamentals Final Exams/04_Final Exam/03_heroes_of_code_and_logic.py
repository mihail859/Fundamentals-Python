n = int(input())
heroes_dict = dict()

for _ in range(n):
    input_line = input().split()
    name = input_line[0]
    hp = int(input_line[1])
    mp = int(input_line[2])
    heroes_dict[name] = {'hp': hp, 'mp': mp}

print(heroes_dict)