def sum_even_odd(num, even, odd):
    for i in range(len(num)):
        if int(num[i]) % 2 != 0:
            odd += int(num[i])

        else:
            even += int(num[i])
    print(f"Odd sum = {odd}, "
          f"Even sum = {even}")


number = input()
sum_even = 0
sum_odd = 0
sum_even_odd(number, sum_even, sum_odd)
