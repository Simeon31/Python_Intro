people = {"Jonh": 10, "Jim": 25}
values = dict(Harry=10, Jerry=25)
print(people.keys())
print(people.values())
print(people.items())

# indexing as well as assignment is applicable

# iteration
for key, value in people.items():
    print(key, value)
