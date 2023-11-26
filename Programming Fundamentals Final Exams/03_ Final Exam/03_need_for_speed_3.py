def drive(dictionary, name, interval, tank_fuel):
    if tank_fuel > dictionary[name]["fuel"]:
        print("Not enough fuel to make that ride")
    else:
        dictionary[name]["fuel"] -= tank_fuel
        dictionary[name]["mileage"] += interval
        print(f"{name} driven for {interval} kilometers. {tank_fuel} liters of fuel consumed.")
        if dictionary[name]["mileage"] > 100000:
            print(f"Time to sell the {name}!")
            del dictionary[name]
    return dictionary


def refuel(dictionary, name, tank_fuel):
    before_fuel = dictionary[name]['fuel']
    dictionary[name]['fuel'] += tank_fuel
    if dictionary[name]['fuel'] > 75:
        dictionary[name]['fuel'] = 75
        print(f"{name} refueled with {75-before_fuel} liters")
    else:
        print(f"{name} refueled with {tank_fuel} liters")
    return dictionary


def revert(dictionary, name, km):
    dictionary[name]['mileage'] -= km
    print(f"{name} mileage decreased by {km} kilometers")
    if dictionary[name]['mileage'] < 10000:
        dictionary[name]['mileage'] = 10000
    return dictionary


n = int(input())
car_dict = dict()

for _ in range(n):
    input_data = input().split("|")
    car = input_data[0]
    mileage = int(input_data[1])
    fuel = int(input_data[2])
    car_dict[car] = {"mileage": mileage, "fuel": fuel}

while True:
    command, *params = input().split(' : ')
    if command == "Stop":
        break

    elif command == "Drive":
        car_name = params[0]
        distance = int(params[1])
        fuel = int(params[2])
        car_dict = drive(car_dict, car_name, distance, fuel)

    elif command == 'Refuel':
        car_name = params[0]
        fuel = int(params[1])
        car_dict = refuel(car_dict, car_name, fuel)

    elif command == 'Revert':
        car_name = params[0]
        kilometers = int(params[1])
        car_dict = revert(car_dict, car_name, kilometers)

for key, value in car_dict.items():
    mileage_car = value['mileage']
    fuel_car = value['fuel']
    print(f"{key} -> Mileage: {mileage_car} kms, Fuel in the tank: {fuel_car} lt.")