employees_happiness = [int(x) for x in input().split()]
factor_c = int(input())
employees_happiness = [employees_happiness[x] * factor_c for x in range(len(employees_happiness))]
average_happiness = sum(employees_happiness) / len(employees_happiness)
happy_employees = list(filter(lambda x: x > average_happiness, employees_happiness))
happy_count = len(happy_employees)

if happy_count >= len(employees_happiness) / 2:
    print(f"Score: {happy_count}/{len(employees_happiness)}. Employees are happy!")

else:
    print(f"Score: {happy_count}/{len(employees_happiness)}. Employees are not happy!")