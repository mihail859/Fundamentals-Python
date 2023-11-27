import re

n = int(input())

pattern = r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'

for _ in range(n):
    input_line = input()
    barcode_group = ""
    result = re.match(pattern, input_line)
    if result:
        digits = re.findall(r'\d', input_line)
        if digits:
            for el in digits:
                barcode_group = "".join(digits)
        else:
            barcode_group = "00"

        print(f"Product group: {barcode_group}")

    else:
        print("Invalid barcode")
