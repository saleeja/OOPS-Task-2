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

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

shapes = [Triangle, Square, Pentagon, Circle]

for shape_class in shapes:
    print(f"\nCalculating the area for a {shape_class.__name__}")
    if shape_class == Triangle:
        shape = shape_class(get_float_input("Enter the base of the triangle: "), get_float_input("Enter the height of the triangle: "))
    elif shape_class == Square:
        shape = shape_class(get_float_input("Enter the side of the square: "))
    elif shape_class == Pentagon:
        shape = shape_class(get_float_input("Enter the side of the pentagon: "))
    elif shape_class == Circle:
        shape = shape_class(get_float_input("Enter the radius of the circle: "))
    
    print(f"{shape_class.__name__} area: {shape.area()}")

