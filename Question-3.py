"""3) Add 4 different subclasses for class Shape. - Triangle, Square, Pentagon, Circle.
Define constructor for each of them to assign the necessary parameters required for calculating the area.
Define the area method for each of the classes. When invoked it Should return the area of the shape by calculating it.
Create an object for each of the subclasses and call the area method on the objects."""

from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
     
        raise NotImplementedError("The 'area' method must be implemented by subclasses.")

class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Pentagon(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
       
        s = 5 * self.side / 2
        return math.sqrt(s * (s - self.side) * (s - self.side) * (s - self.side) * (s - self.side)) / 4

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


triangle = Triangle(5, 3)
square = Square(4)
pentagon = Pentagon(5)
circle = Circle(2)

print(f"Triangle area: {triangle.area()}")
print(f"Square area: {square.area()}")
print(f"Pentagon area: {pentagon.area()}")
print(f"Circle area: {circle.area()}")
