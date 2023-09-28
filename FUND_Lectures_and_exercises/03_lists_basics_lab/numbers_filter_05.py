numbers = []
n = int(input())
for _ in range(n):
    number = int(input())
    numbers.append(number)
filter_word = input()
filtered_numbers = []
if filter_word == 'even':
    filtered_numbers = [numbers[i] for i in range(len(numbers)) if numbers[i] % 2 == 0]
elif filter_word == 'odd':
    filtered_numbers = [numbers[i] for i in range(len(numbers)) if numbers[i] % 2 != 0]
elif filter_word == 'negative':
    filtered_numbers = [numbers[i] for i in range(len(numbers)) if numbers[i] < 0]
elif filter_word == 'positive':
    filtered_numbers = [numbers[i] for i in range(len(numbers)) if numbers[i] >= 0]

print(filtered_numbers)