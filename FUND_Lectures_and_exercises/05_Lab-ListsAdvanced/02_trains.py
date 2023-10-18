def add_people(wagons, people):
    wagons[-1] += people
    return wagons


def insert_people(wagon, idx, people):
    wagon[idx] += people
    return wagon


def leave_people(wagon, idx, people):
    wagon[idx] -= people
    return wagon


number = int(input())
wagons_list = [0] * number

while True:
    command = input()
    if command == 'End':
        print(wagons_list)
        break
    command1, *params = command.split(' ')
    if command1 == 'add':
        people_count = int(params[0])
        wagons_list = add_people(wagons_list, people_count)
    elif command1 == 'insert':
        index = int(params[0])
        people_count = int(params[1])
        wagons_list = insert_people(wagons_list, index, people_count)
    elif command1 == 'leave':
        index = int(params[0])
        people_count = int(params[1])
        wagons_list = leave_people(wagons_list, index, people_count)
