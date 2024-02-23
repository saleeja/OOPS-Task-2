"""1) Create a class named Shape. Add an instance method called area. But don't define the method, just raise
NotImplementedError() exception with a suitable message"""


class Shape:
    def area(self):
        raise NotImplementedError("NotImplementedError.")


class Square(Shape):
    def __init__(self, side):
        self.side = side

# instance
square = Square(4)

# Calling area directly will raise the NotImplementedError
square_area = square.area()
