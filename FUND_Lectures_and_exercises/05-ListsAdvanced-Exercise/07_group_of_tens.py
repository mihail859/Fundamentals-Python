numbers = [int(x) for x in input().split(', ')]

boundary = 10
while numbers:
    curr_group = [x for x in numbers if x <= boundary]
    print(f"Group of {boundary}'s: {curr_group}")

    boundary += 10
    numbers = [x for x in numbers if x not in curr_group]