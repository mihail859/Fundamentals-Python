special_sums = [5, 7, 11]
n = int(input())
for number in range(1, n + 1):
    sum_numbers = 0
    for j in range(len(str(number))):
        sum_numbers += int(str(number)[j])
    if sum_numbers in special_sums:
        print(f'{number} -> True')
    else:
        print(f'{number} -> False')