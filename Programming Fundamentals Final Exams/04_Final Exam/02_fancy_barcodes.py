import re

n = int(input())

pattern = r'(@)(#+)(?P<product>[A-Z][A-Za-z0-9]{5,})\1\2'

products = []
for _ in range(n):
    input_line = input()
    result = re.finditer(pattern, input_line)
    for p in result:
        product = p.group('product')
        products.append(product)
print(products)
