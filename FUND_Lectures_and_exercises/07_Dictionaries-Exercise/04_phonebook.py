contacts = {}
n = None
while True:
    input_data = input().split("-")
    if input_data[0].isdigit():
        n = int(input_data[0])
        break
    name = input_data[0]
    phone_number= input_data[1]

    contacts[name] = phone_number

for i in range(n):
    searched_contact = input()
    if searched_contact in contacts.keys():
        print(f"{searched_contact} -> {contacts[searched_contact]}")
    else:
        print(f"Contact {searched_contact} does not exist.")