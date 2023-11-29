def cast_spell(dictionary, hero, mp, spell):
    if dictionary[hero]['mp'] > mp:
        dictionary[hero]['mp'] -= mp
        left_mp = dictionary[hero]['mp']
        print(f"{hero} has successfully cast {spell} and now has {left_mp} MP!")

    else:
        print(f"{hero} does not have enough MP to cast {spell}!")

    return dictionary


def take_damage(dictionary, hero, damage, attacker):
    pass


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
