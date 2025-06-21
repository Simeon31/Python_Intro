class Point:
    default_color = "orange"
    def __init__(self, x, y): # magic method
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Drawing Point: ({self.x}, {self.y})")

    def __eq__(self, other): # magic method
        return self.x == other.x and self.y == other.y

    def __add__(self, other): # magic method
        return Point(self.x + other.x, self.y + other.y)

point = Point.zero()
point.draw()
print(point.default_color)

# Objects comparison
first_point = Point(1, 1)
second_point = Point(1, 1)
print(first_point == second_point)

# Arithmetic operations
combined_point = first_point + second_point
print(combined_point.y)