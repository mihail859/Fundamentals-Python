list_numbers = [int(x) for x in input().split()]
numbers_to_remove = int(input())
len_list = len(list_numbers)
new = list_numbers.copy()
new.sort(reverse=False)

removed_numbers = []
for i in range(numbers_to_remove):
    removed_numbers.append(new[i])

final_list = list_numbers.copy()
for j in range(len_list):
    number = list_numbers[j]
    for k in range(len(removed_numbers)):
        removed = removed_numbers[k]
        if number == removed:
            final_list.remove(number)
            break
final_list = [str(x) for x in final_list]
print(", ".join(final_list))