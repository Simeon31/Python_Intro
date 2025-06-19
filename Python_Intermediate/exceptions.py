from timeit import timeit

# Exception handling
try:
    # Another approach might be the with statement clause, which automatically releases the resource
    with open("arrays.py") as file02:
         print("Opening file")
    file01 = open("exceptions.py")
    age = int(input("Age: "))
    xfactor = 10 / 0
except (ValueError, ZeroDivisionError):
    print("Invalid value")
else:
    print("Age is: ", age)
finally:
    file01.close()

# Raising exception
test01 = """
def calculate_age(age):
    if age <= 0:
        raise ValueError("Age must be greater than zero")
    return 10 / age

try:
    calculate_age(0)
except ValueError as ex:
    pass
"""

test02 = """
# Raising exception
def calculate_age(age):
    if age <= 0:
      return None
    return 10 / age

xfactor = calculate_age(-1)
if xfactor is not None:
    pass
"""

print("Test01: ", timeit(test01, number=10_000))
print("Test02: ", timeit(test02, number=10_000))