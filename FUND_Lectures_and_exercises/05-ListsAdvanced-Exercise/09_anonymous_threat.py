def merged(list1, st, ending):
    merged_words = ""
    for i in range(st, ending + 1):
        w = list1[i]
        merged_words += w
    return merged_words


words = input().split(" ")

while True:
    line = input()
    if line == '3:1':
        break

    command, start, end = line.split(' ')

    if command == 'merge':
        start_idx = int(start)
        end_idx = int(end)

        start_idx = max(0, start_idx)
        end_idx = min(len(words) - 1, end_idx)

        if start_idx >= end_idx:
            continue

        merged_el = merged(words, start_idx, end_idx)
        removed_el = end_idx - start_idx + 1
        for _ in range(removed_el):
            words.pop(start_idx)

        words.insert(start_idx, merged_el)

    elif command == 'divide':
        el_idx = int(start)
        partition = int(end)

        element = words[el_idx]
        el_parts = []
        part_size = len(element) // partition

        current_partition = ''
        for idx in range((partition - 1) * part_size):
            current_partition += element[idx]
            if len(current_partition) == part_size:
                el_parts.append(current_partition)
                current_partition = ''
        current_partition = ''
        for idx in range((partition - 1) * part_size, len(element)):
            current_partition += element[idx]
        el_parts.append(current_partition)

        words.pop(el_idx)

        for idx in range(len(el_parts)):
            words.insert(el_idx + idx, el_parts[idx])

print(" ".join(words))

