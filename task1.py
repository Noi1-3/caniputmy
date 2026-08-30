import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def length(self):
        return 2 * math.pi * self.radius

    def __lt__(self, other):
        return self.length() < other.length()

    def __le__(self, other):
        return self.length() <= other.length()

    def __gt__(self, other):
        return self.length() > other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    def __add__(self, value):
        return Circle(self.radius + value)

    def __sub__(self, value):
        return Circle(self.radius - value)

    def __iadd__(self, value):
        self.radius += value
        return self

    def __isub__(self, value):
        self.radius -= value
        return self

c1 = Circle(5)
c2 = Circle(10)
print("радиус c1:", c1.radius, "радиус c2:", c2.radius)
print("c1 == c2:", c1 == c2)
print("c1 < c2:", c1 < c2)
c1 += 2
print("радиус c1 после += 2:", c1.radius)