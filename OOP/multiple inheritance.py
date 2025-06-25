class Employee:
    def greet(self):
        print("Employee says Hello")

class Person:
    def greet(self):
        print("Person says Hello")

class Manager(Person, Employee):
    pass

manager = Manager()
manager.greet() # executes the first method of the first given class in the constructor