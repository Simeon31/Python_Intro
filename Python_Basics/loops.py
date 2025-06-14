i:int = 1

# while loop
while i <= 10:
    print(i * '*')
    i += 1
print('-' * 10)

#for loop

# simple iteration
for i in range(10):
    print(i, (i + 1) * '.')
print('-' * 10)

# iteration with given range
for i in range(1, 10):
    print(i)
print('-' * 10)

# iteration with steps
for i in range(1, 10, 2):
    print(i)
