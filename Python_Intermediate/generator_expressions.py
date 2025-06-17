from sys import getsizeof

gen = (x * 2 for x in range(100000))
list = [x * 2 for x in range(100000)]

# memory usage comparison
print("Generator: ", getsizeof(gen))
print("List: ", getsizeof(list))