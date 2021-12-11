import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    pass


class Circle(Figure):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
        self.ab = self.length_from_radius_to_center()
        self.perimeter = self.ab * 2 * math.pi
        self.area = self.ab ** 2 * math.pi

    def length_from_radius_to_center(self):
        x1 = self.a.x
        y1 = self.a.y
        x2 = self.b.x
        y2 = self.b.y

        ab = abs((x2 - x1) + (y2 - y1))
        return ab


class Triangle(Figure):
    # прямоугольный треугольник
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.ab = self.sides()[0]  # катет ab треугольника
        self.bc = self.sides()[1]  # катет bc треугольника
        self.ac = self.sides()[2]  # гепотенуза ac треугольника
        self.perimeter = self.ab + self.bc + self.ac
        self.area = self.ab * self.bc / 2

    def sides(self):
        x1 = self.a.x
        y1 = self.a.y
        x2 = self.b.x
        y2 = self.b.y
        x3 = self.c.x
        y3 = self.c.y

        ab = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        bc = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        ac = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
        return ab, bc, ac


class Square(Figure):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
        self.ab = self.sides()
        self.perimeter = self.ab * 4
        self.area = self.ab ** 2

    def sides(self):
        x1 = self.a.x
        y1 = self.a.y
        x2 = self.b.x
        y2 = self.b.y

        ab = abs((x2 - x1) + (y2 - y1))
        return ab


if __name__ == '__main__':

    center_circle = Point(2, 0)
    radius_length = Point(4, 0)
    c = Circle(center_circle, radius_length)

    coord_a_triangle = Point(0, 0)
    coord_b_triangle = Point(4, 0)
    coord_c_triangle = Point(4, 3)
    t = Triangle(coord_a_triangle, coord_b_triangle, coord_c_triangle)

    coord_a_square = Point(6, 0)
    coord_b_square = Point(4, 0)
    s = Square(coord_a_square, coord_b_square)

    my_list = [c, t, s]
    for area_figure in my_list:
        if area_figure == my_list[0]:
            print(f"Area of square: {area_figure.area}")
        elif area_figure == my_list[1]:
            print(f"Area of circle: {area_figure.area}")
        elif area_figure == my_list[2]:
            print(f"Area of triangle: {area_figure.area}")