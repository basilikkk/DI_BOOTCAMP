import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self._radius = radius
        elif diameter is not None:
            self._radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be provided.")

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

    def area(self):
        return math.pi * (self._radius ** 2)

    def __str__(self):
        return f"Circle with radius: {self._radius}"

    def __repr__(self):
        return f"Circle(radius={self._radius})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self._radius + other._radius)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self._radius < other._radius
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self._radius == other._radius
        return NotImplemented

# Example usage:

c1 = Circle(radius=3)
c2 = Circle(diameter=8)
c3 = Circle(radius=4)

print(c1)  # Circle with radius: 3
print(c1.radius)  # 3
print(c1.diameter)  # 6
print(c1.area())  # 28.274333882308138

c4 = c1 + c3
print(c4)  # Circle with radius: 7

print(c1 < c3)  # True
print(c1 == Circle(radius=3))  # True

# Putting circles in a list and sorting them
circles = [c1, c2, c3, c4]
circles.sort()
print(circles)  # Sorted list of circles by radius
