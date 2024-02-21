class Rectangle:
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2

    def perimetr(self):
        print(f'Периметр прямоугольника = {2 * (self.side_1 + self.side_2)}')

    def area(self):
        print(f'Площадь прямоугольника = {self.side_1 * self.side_2}')


rectangle = Rectangle(6, 7)
rectangle.perimetr()
rectangle.area()
