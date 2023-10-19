list_of_numbers = [x for x in input().split(", ")]
positives_nums = [x for x in list_of_numbers if int(x) >= 0]
negatives_nums = [x for x in list_of_numbers if int(x) < 0]
even_nums = [x for x in list_of_numbers if int(x) % 2 == 0]
odd_nums = [x for x in list_of_numbers if int(x) % 2 != 0]

print(f'Positive: {", ".join(positives_nums)}')
print(f'Negative: {", ".join(negatives_nums)}')
print(f'Even: {", ".join(even_nums)}')
print(f'Odd: {", ".join(odd_nums)}')