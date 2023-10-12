def sum_numbers(n1, n2):
    return n1 + n2

def subtract(n1, n2, n3):
    return sum_numbers(n1, n2) - n3


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
print(subtract(num_1, num_2, num_3))