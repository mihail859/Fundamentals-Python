#cheese 10 bread 5 ham 10 chocolate 3
input_line = input().split()
searched_products = input().split()
products = dict()
for i in range(0, len(input_line), 2):
    product_key = input_line[i]
    quantity = int(input_line[i + 1])
    products[product_key] = quantity

for j in range(len(searched_products)):
    searched_product = searched_products[j]
    if searched_product in products.keys():
        print(f"We have {products[searched_product]} of {searched_product} left")

    else:
        print(f"Sorry, we don't have {searched_product}")