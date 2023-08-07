def cast_spell(dictionary, hero, mp, name):
    mp = int(mp)
    if dictionary[hero]['MP'] >= mp:
        dictionary[hero]['MP'] -= mp

        print(f"{hero} has successfully cast {name} and now has {dictionary[hero]['MP']} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {name}!")

    return dictionary


def take_damage(dictionary, hero, damage_points, attacker_name):
    damage_points = int(damage_points)
    dictionary[hero]['HP'] -= damage_points
    if dictionary[hero]['HP'] > 0:
        print(f"{hero} was hit for {damage_points} HP by {attacker_name} "
              f"and now has {dictionary[hero]['HP']} HP left!")
    else:
        print(f"{hero} has been killed by {attacker_name}!")
        del dictionary[hero]
    return dictionary


def recharge(dictionary, hero1, increase):  # -> MP
    increase = int(increase)
    hp_increase = increase
    dictionary[hero1]['MP'] += increase
    if dictionary[hero1]['MP'] > 200:
        hp_increase = increase - (dictionary[hero1]['MP'] - 200)
        dictionary[hero1]['MP'] = 200
    print(f"{hero1} recharged for {hp_increase} MP!")

    return dictionary


def heal(dictionary, hero1, increase):  # -> HP
    increase = int(increase)
    hp_increase = increase
    dictionary[hero1]['HP'] += increase
    if dictionary[hero1]['HP'] > 100:
        hp_increase = increase - (dictionary[hero1]['HP'] - 100)
        dictionary[hero1]['HP'] = 100
    print(f"{hero1} healed for {hp_increase} HP!")

    return dictionary


# dictionary_example -> {'hero name': {'HP': 100, 'MP': 200}}
# a hero can have a maximum of 100 HP and 200 MP


heroes_dictionary = {}
number_of_heroes = int(input())
# Create the heroes in my dictionary
for _ in range(number_of_heroes):
    hero_data = input().split()
    heroes_dictionary[hero_data[0]] = {"HP": int(hero_data[1]), "MP": int(hero_data[2])}

# start the game inside the while loop
while True:
    command, *params = input().split(" - ")
    if command == "End":
        break

    if command == "CastSpell":  # {hero name} – {MP needed} – {spell name}"
        hero_name, mp_needed, spell_name = params
        heroes_dictionary = cast_spell(heroes_dictionary, hero_name, mp_needed, spell_name)

    elif command == "TakeDamage":  # {hero name} – {damage} – {attacker}
        hero_name, damage, attacker = params
        heroes_dictionary = take_damage(heroes_dictionary, hero_name, damage, attacker)

    elif command == "Recharge":  # {hero name} – {amount}
        hero, amount = params
        heroes_dictionary = recharge(heroes_dictionary, hero, amount)

    elif command == "Heal":
        hero, amount = params
        heroes_dictionary = heal(heroes_dictionary, hero, amount)

for key, data in heroes_dictionary.items():
    hp = data['HP']
    mp = data['MP']
    print(f"{key}\n  HP: {hp}\n  MP: {mp}")
