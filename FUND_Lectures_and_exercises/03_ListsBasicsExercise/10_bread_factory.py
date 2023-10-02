day_events = input().split("|")
initial_energy = 100
initial_coins = 100

is_closed = False
for i in range(len(day_events)):
    split_info = day_events[i].split("-")
    event = split_info[0]
    number = int(split_info[1])
    if event == "rest":
        if initial_energy == 100:
            print("You gained 0 energy.")
        elif initial_energy + number > 100:
            gained = 100 - initial_energy
            initial_energy += gained
            print(f"You gained {gained} energy.")
        else:
            initial_energy += number
            print(f"You gained {number} energy.")

        print(f"Current energy: {initial_energy}.")

    elif event == "order":

        if initial_energy - 30 >= 0:
            initial_coins += number
            initial_energy -= 30
            print(f"You earned {number} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
    else:
        if initial_coins - number >= 0:
            initial_coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            is_closed = True
            break
if not is_closed:
    print(f"Day completed!\nCoins: {initial_coins}\nEnergy: {initial_energy}")