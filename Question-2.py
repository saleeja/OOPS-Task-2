"""2) Make it an abstract base class by inheriting ABC class from the abc module. (To import: from abc import ABC)
Make the area method an abstract method by decorating it with abstractmethod decorator (import this also from 
abc)."""


from abc import ABC, abstractmethod 
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        raise NotImplementedError("The 'area' method must be implemented by subclasses.")

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

# Create instances of concrete subclasses:
circle = Circle(21)
square = Square(20)

# Calculate areas using the implemented methods:
circle_area = circle.area()
square_area = square.area()

print(f"Circle area: {circle_area}")  # Output: Circle area: 78.53981633974483
print(f"Square area: {square_area}")  # Output: Square area: 16
