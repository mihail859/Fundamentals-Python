list_input = input().split()
even_len_items = [i for i in list_input if len(i) % 2 == 0]
for j in even_len_items:
    print(j)