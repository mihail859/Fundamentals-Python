string_input = input().split(" ")
new_strings = [w * len(w) for w in string_input]
print("".join(new_strings))