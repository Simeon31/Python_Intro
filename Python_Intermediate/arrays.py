from array import array

numbers = array("i", [1, 2, 3, 4, 5])

numbers.append(6)
numbers.remove(3)

for number in numbers:
    print(number)