#!/usr/bin/python3

from abc import ABC, abstractmethod
# Importing ABC (Abstract Base Class) and abstractmethod from the abc module.
from math import pi
# Importing the mathematical constant pi from the math module.

class Shape(ABC):
    # Define an abstract base class Shape inheriting from ABC (Abstract Base Class).

    @abstractmethod
    def area(self):
        # Abstract method to calculate the area of the shape.
        pass

    @abstractmethod
    def perimeter(self):
        # Abstract method to calculate the perimeter of the shape.
        pass


class Circle(Shape):
    # Define a concrete class Circle that inherits from Shape.

    def __init__(self, radius):
        # Constructor method to initialize a Circle object with a given radius.
        self.radius = radius

    def area(self):
        # Method to calculate the area of the circle.
        return pi * self.radius ** 2

    def perimeter(self):
        # Method to calculate the perimeter (circumference) of the circle.
        return 2 * pi * abs(self.radius)


class Rectangle(Shape):
    # Define a concrete class Rectangle that inherits from Shape.

    def __init__(self, width, height):
        # Constructor method to initialize a Rectangle object with given width and height.
        self.width = width
        self.height = height

    def area(self):
        # Method to calculate the area of the rectangle.
        return self.width * self.height

    def perimeter(self):
        # Method to calculate the perimeter of the rectangle.
        return 2 * (self.width + self.height)


def shape_info(shape):
    # Function to display information about a shape, including its area and perimeter.
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())


# Create instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(3, 4)

# Display information about the Circle
print("Circle:")
shape_info(circle)

# Display information about the Rectangle
print("\nRectangle:")
shape_info(rectangle)

