def is_palindrome(list_numbers):
    for num in list_numbers:
        if num == num[::-1]:
            print('True')
        else:
            print('False')


chars = input().split(', ')
is_palindrome(chars)
