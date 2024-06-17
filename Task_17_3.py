class Shape:
    def __init__(self, colour, square):
        self.colour = colour
        self.square = square

    def info_colour(self):
        print(f"{self.colour}")
    def info_square(self):
        print(f"{self.square}")

a = Shape("Red", 5)
b = Shape("Blue", 10)

a.info_colour()
a.info_square()
b.info_colour()
b.info_square()
