def calculate_order_price(product_order, quantity_of_product, prices):
    order_price = prices[product_order] * quantity_of_product
    return f"{order_price:.2f}"


product = input()
quantity = int(input())
product_prices = {
    "coffee": 1.50,
    "coke": 1.40,
    "water": 1.00,
    "snacks": 2.00
}
print(calculate_order_price(product, quantity, product_prices))
