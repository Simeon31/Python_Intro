products = [
    ("Orange juice", 2),
    ("Cake", 15),
    ("Salad", 5)
]

prices = map(lambda product: product[1], products)

for price in prices:
    print(price)
