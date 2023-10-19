first_list = input().split(', ')
second_list = input().split(', ')
matched_list = []

for element in first_list:
    for el2 in second_list:
        if element in el2:
            matched_list.append(element)
            break

print(matched_list)