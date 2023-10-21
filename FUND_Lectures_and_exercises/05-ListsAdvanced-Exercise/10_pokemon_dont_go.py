def remove_function(sequence, idx, all_removed_elements):
    if idx < 0:
        removed_element = sequence[0]
        sequence[0] = sequence[-1]

    elif idx > len(sequence) - 1:
        removed_element = sequence[-1]
        sequence[-1] = sequence[0]
    else:
        removed_element = sequence[idx]
        sequence.pop(idx)

    all_removed_elements += removed_element
    for i in range(len(sequence)):
        if sequence[i] <= removed_element:
            sequence[i] += removed_element

        else:
            sequence[i] -= removed_element

    return all_removed_elements


input_sequence = [int(x) for x in input().split()]
sum_removed = 0
while input_sequence:
    index = int(input())
    sum_removed = remove_function(input_sequence, index, sum_removed)

print(sum_removed)