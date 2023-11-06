def register(parking, username, license_plate_number):
    if username not in parking.keys():
        parking[username] = license_plate_number
        print(f"{username} registered {license_plate_number} successfully")

    elif username in parking.keys():
        print(f"ERROR: already registered with plate number {parking[username]}")
    return parking


def unregister(parking, username):
    if username not in parking.keys():
        print(f"ERROR: user {username} not found")
    else:
        print(f"{username} unregistered successfully")
        del parking[username]
    return parking


parking_dict = dict()
n = int(input())
for i in range(n):
    command, *params = input().split(' ')
    if command == 'register':
        user = params[0]
        license_number = params[1]
        parking_dict = register(parking_dict, user, license_number)
    elif command == 'unregister':
        user = params[0]
        parking_dict = unregister(parking_dict, user)

for key, value in parking_dict.items():
    print(f"{key} => {value}")
