def absolute_values(list_of_numbers):
    list_of_numbers = [abs(x) for x in list_of_numbers]
    return list_of_numbers


list_nums = [float(x) for x in input().split()]
print(absolute_values(list_nums))
