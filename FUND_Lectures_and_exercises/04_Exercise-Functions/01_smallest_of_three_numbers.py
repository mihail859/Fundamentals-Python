def smallest(list_of_numbers):
    return min(list_of_numbers)


numbers = []
for i in range(3):
    number = int(input())
    numbers.append(number)
print(smallest(numbers))
