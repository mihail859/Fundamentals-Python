def cast_spell(dictionary, hero, mp, spell):
    if dictionary[hero]['mp'] > mp:
        dictionary[hero]['mp'] -= mp
        left_mp = dictionary[hero]['mp']
        print(f"{hero} has successfully cast {spell} and now has {left_mp} MP!")

    else:
        print(f"{hero} does not have enough MP to cast {spell}!")

    return dictionary


def take_damage(dictionary, hero, damage, attacker):
    dictionary[hero]['hp'] -= damage
    if dictionary[hero]['hp'] > 0:
        current_hp = dictionary[hero]['hp']
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")

    else:
        del dictionary[hero]
        print(f"{hero} has been killed by {attacker}!")

    return dictionary


def recharge(dictionary, hero, amount):
    current_amount = dictionary[hero]['mp']
    dictionary[hero]['mp'] += amount
    if dictionary[hero]['mp'] >= 200:
        dictionary[hero]['mp'] = 200
        print(f"{hero} recharged for {200 - current_amount} MP!")
    else:
        print(f"{hero} recharged for {amount} MP!")

    return dictionary


def heal(dictionary, hero, amount):
    current_amount = dictionary[hero]['hp']
    dictionary[hero]['hp'] += amount
    if dictionary[hero]['hp'] >= 100:
        dictionary[hero]['hp'] = 100
        print(f"{hero} healed for {100 - current_amount} HP!")
    else:
        print(f"{hero} healed for {amount} HP!")

    return dictionary


n = int(input())
heroes_dict = dict()

for _ in range(n):
    input_line = input().split()
    name = input_line[0]
    hit_points = int(input_line[1])
    mana_points = int(input_line[2])
    heroes_dict[name] = {'hp': hit_points, 'mp': mana_points}

while True:
    command, *params = input().split(" - ")
    if command == "End":
        break

    elif command == "CastSpell":
        hero_name = params[0]
        mp_needed = int(params[1])
        spell_name = params[2]
        heroes_dict = cast_spell(heroes_dict, hero_name, mp_needed, spell_name)

    elif command == "TakeDamage":
        hero_name = params[0]
        damage_points = int(params[1])
        attacker_name = params[2]
        heroes_dict = take_damage(heroes_dict, hero_name, damage_points, attacker_name)

    elif command == "Recharge":
        hero_name = params[0]
        amount_changed = int(params[1])
        heroes_dict = recharge(heroes_dict, hero_name, amount_changed)

    elif command == "Heal":
        hero_name = params[0]
        amount_changed = int(params[1])
        heroes_dict = heal(heroes_dict, hero_name, amount_changed)

for key, value in heroes_dict.items():
    print(key)
    print(f"  HP: {value['hp']}")
    print(f"  MP: {value['mp']}")