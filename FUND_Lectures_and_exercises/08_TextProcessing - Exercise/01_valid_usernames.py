import re


def is_valid_username(username):
    pattern = re.compile(r'^[a-zA-Z0-9_-]{3,16}$')
    return bool(pattern.match(username))


usernames = input().split(", ")

valid_usernames = [username for username in usernames if is_valid_username(username)]
print("\n".join(valid_usernames))
