from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1, p2)
print(f"x: {p1.x} y: {p1.y}")
