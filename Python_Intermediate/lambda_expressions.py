products = [
    ("Pizza", 20),
    ("Burger", 15),
    ("Fries", 5)
]

products.sort(key=lambda product: product[1], reverse=False)
print(*products)