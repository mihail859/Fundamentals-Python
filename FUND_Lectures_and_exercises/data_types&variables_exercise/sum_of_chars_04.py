n = int(input())
list_of_letters = []
for i in range(n):
    letter_value = ord(input())
    list_of_letters.append(letter_value)

print(f"The sum equals: {sum(list_of_letters)}")
