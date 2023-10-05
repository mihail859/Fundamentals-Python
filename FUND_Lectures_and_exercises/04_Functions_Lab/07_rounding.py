numbers = [float(x) for x in input().split()]
rounded_numbers = list(map(lambda x: round(x), numbers))
print(rounded_numbers)