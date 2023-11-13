while True:
    string = input()
    if string == "end":
        break
    else:
        print(f"{string} = {''.join(list(reversed(string)))}")
