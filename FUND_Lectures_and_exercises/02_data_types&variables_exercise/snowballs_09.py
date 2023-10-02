snowballs_values_dict = {}
snowballs_list = []
number_of_snowballs = int(input())
for i in range(number_of_snowballs):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    value = (weight / time_needed) ** quality

    snowballs_values_dict = {'w': weight, 't': time_needed, 'v': value, 'q': quality}
    snowballs_list.append(snowballs_values_dict)
highest = max(snowballs_list, key=lambda x: x['v'])
print(f"{highest['w']} : {highest['t']} = {int(highest['v'])} ({highest['q']})")