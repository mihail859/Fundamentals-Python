def password_validator(password):
    is_valid = True
    if len(password) not in range(6, 11):
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    count_digits = 0
    for i in range(len(password)):
        char_curr = password[i]
        if char_curr.isdigit():
            count_digits += 1
    if count_digits < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")

password_input = input()
password_validator(password_input)
