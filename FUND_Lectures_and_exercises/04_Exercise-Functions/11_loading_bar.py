def loading_bar(num):
    if num == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    else:
        load_bar = f'{num}% [{(num // 10) * "%"}{(10 - (num // 10)) * "."}]\n' \
                   f'Still loading{"." * 3}'
        return load_bar


number = int(input())
print(loading_bar(number))
