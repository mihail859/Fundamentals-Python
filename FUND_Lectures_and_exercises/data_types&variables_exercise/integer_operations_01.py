result = 0
for i in range(1, 5):
    number = int(input())
    if i <= 2:
        result += number
    elif i == 3:
        result = result // number
    else:
        result *= number

print(result)