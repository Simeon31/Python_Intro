numbers = [1, 2, 2, 3, 3, 4, 5]

unique_numbers = set(numbers)
print(unique_numbers)

sets = {1, 2, 0}
sets.add(6)
sets.remove(6)
print(sets)

# union
print("Union: ", unique_numbers | sets)

# intersection
print("Intersection: ", unique_numbers & sets)

# difference
print("Difference: ", unique_numbers - sets)

# symmetric difference
print("Symmetric difference: ", unique_numbers ^ sets)