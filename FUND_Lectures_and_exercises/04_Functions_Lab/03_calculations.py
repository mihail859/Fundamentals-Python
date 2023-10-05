def calculate(process, fn, sn):
    if process == "multiply":
        return fn * sn
    elif process == "divide":
        return int(fn / sn)
    elif process == "add":
        return fn + sn
    elif process == "subtract":
        return fn - sn


operator = input()
first_number = int(input())
second_number = int(input())
print(calculate(operator, first_number, second_number))
