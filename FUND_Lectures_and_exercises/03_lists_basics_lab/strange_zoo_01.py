animal_parts = []
# the tail, the body, and the head
for _ in range(3):
    body_part = input()
    animal_parts.append(body_part)
animal_parts[0], animal_parts[2] = animal_parts[2], animal_parts[0]
print(animal_parts)