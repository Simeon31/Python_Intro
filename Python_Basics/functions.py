def greet_user():
    print("Hello user!")

greet_user()

print('-' * 10)

# function with params
def say_hello(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

say_hello("John", "Smith")

# return type functions
def greet_user(first_name, last_name):
    return f"Hello, {first_name} {last_name}!"

greeting = greet_user("John", "Smith")

print('-' * 10)

# using xargs
def get_numbers(*numbers):
    print(f"Your numbers: {numbers}")

get_numbers(1, 2, 3)

