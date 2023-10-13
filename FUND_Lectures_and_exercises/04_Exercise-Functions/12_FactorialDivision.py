from math import factorial


def factorial_division(num1, num2):
    result = factorial(num1) / factorial(num2)
    return result


number1 = int(input())
number2 = int(input())
print(f"{factorial_division(number1, number2):.2f}")
