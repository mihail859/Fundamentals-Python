numbers = [int(x) for x in input().split(', ')]
found_indices = map(
    lambda x: x if numbers[x] % 2 == 0 else 'no',
    range(len(numbers))
)
even_indices = list(filter(
    lambda a:  a != 'no',
    found_indices
))
print(even_indices)