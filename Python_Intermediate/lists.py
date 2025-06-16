letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# having a repeated values for List
zeros = [0] * 50

# combining lists
combined = letters + zeros
print(combined)

print('-' * 30)

numbers = list(range(11))
print(numbers)

print('-' * 30)

# reversing a list
print(numbers[::-1])

print('-' * 30)

# unpacking a list
first_char, second_char, third_char, *others = letters
print(second_char)
print(others)

print('-' * 30)

# iterating over a list
for index, letter in enumerate(letters):
    print(index, letter)

print('-' * 30)

# inserting elements
numbers.append(11)
numbers.insert(2, 2)
print(*numbers)

# removing elements
letters.pop() # deletes last element
letters.pop(2) # index deletion
letters.remove('a') # removes by element
del letters[::2] # deletes by given range
print(*letters)

print('-' * 30)

# finding elements
if 'h' in letters:
    print(letters.index('h'))

print('-' * 30)

# sorting list
numbers.sort(reverse=True) # reverse in descending order
print(numbers)