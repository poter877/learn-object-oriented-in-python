class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return self.width * 2 + self.length * 2


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length=length, width=length)
