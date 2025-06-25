class Animal:
    def __init__(self, age):
        print("Animal constructor")
        self.age = age

    def eat(self):
        print("Animal eats")

class Mammal(Animal):
    def __init__(self, weight, age):
        super().__init__(age)
        print("Mammal constructor")
        self.weight = weight

    def move(self):
        print("Mammal moves")

class Eagle(Animal):
    def move(self):
        print("Mammal moves")

    def hunt(self):
        print("Eagle hunts")

eagle = Eagle(20)
eagle.eat()
print("Age:", eagle.age)
print(isinstance(eagle, Animal))
print(issubclass(Eagle, Animal))

mammal = Mammal(80, 20)
print("Age:", mammal.age)
print("Weight:", mammal.weight)