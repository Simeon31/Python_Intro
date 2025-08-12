import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(type(arr))
print(arr.shape)

arr02 = np.zeros((2, 3), dtype=int)
print(arr02)

arr03 = np.ones((3, 3), dtype=int)
print(arr03)

arr04 = np.full((3, 3), 8, dtype=int)
print(arr04)

arr05 = np.random.random((3, 3))
print(arr05)
print(arr05[1, 2])
print(arr05 > 0.3)
print(arr05[arr05 > 0.4]) # boolean indexing

print("Sum of arr04: ", np.sum(arr04))
print("Rounding of arr05:\n", np.round(arr05))

# Arithmetic operations on arr and numbers
first = np.array([1, 2, 3])
second = np.array([4, 5, 6])
print("Sum of two arrays:", first + second)
print("-" * 40)

dimensions_inch = np.array([4, 5, 6])
dimensions_cm = dimensions_inch * 2.54
print("Dimensions_cm:",  dimensions_cm)