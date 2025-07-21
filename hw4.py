class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle: ширина={self.width}, высота={self.height}"

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

r1 = Rectangle(8, 13)
r2 = Rectangle(5,55)
r3 = r1 + r2
print(r3)