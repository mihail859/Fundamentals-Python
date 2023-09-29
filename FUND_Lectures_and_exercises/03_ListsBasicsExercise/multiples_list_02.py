factor = int(input())
count = int(input())

list_numbers = [factor + (factor * i) for i in range(count)]
print(list_numbers)