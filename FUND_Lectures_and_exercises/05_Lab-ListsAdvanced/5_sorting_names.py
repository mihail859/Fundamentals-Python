names_list = input().split(", ")
sorted_names = sorted(names_list, key=lambda x: (-len(x), x))
print(sorted_names)