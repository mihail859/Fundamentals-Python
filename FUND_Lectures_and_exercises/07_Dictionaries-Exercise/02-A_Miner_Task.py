resource_dict = {}

while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = int(input())
    if resource not in resource_dict.keys():
        resource_dict[resource] = 0
    resource_dict[resource] += quantity

for key, value in resource_dict.items():
    print(f"{key} -> {value}")
