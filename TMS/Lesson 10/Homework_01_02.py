"""
Ex.1
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса Circle (атрибуты: координаты центра, длина радиуса; методы:
нахождение периметра и площади окружности), Triangle (атрибуты: три точки, методы: нахождение площади и периметра),
Square (атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.
"""

import math


# Не до конца пока разобрал реализацию всех 3-ёх классов
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Figure:
    def __init__(self, area=0, perimeter=0):
        self.area = area
        self.perimeter = perimeter


# Без использования Point and Figure
class Square(Figure):
    def __init__(self, coord_a: int, coord_b: int):
        super().__init__()  # по условию надо будет это писать,так как дочерние от Figure
        self.coord_a = coord_a
        self.coord_b = coord_b

    def perimeter_square(self):
        perimeter = (self.coord_a + self.coord_b) * 2
        return perimeter

    def area_square(self):
        area = self.coord_a * self.coord_b
        return area


class Circle(Figure):
    def __init__(self, center_coordinates: int, radius_length: int):
        super().__init__()  # по условию надо будет это писать,так как дочерние от Figure
        self.center_coordinates = center_coordinates
        self.radius_length = radius_length

    def perimeter_circle(self):
        perimeter = self.radius_length * 2
        return perimeter

    def area_circle(self):
        area = math.pi * self.radius_length ** 2
        return area


class Triangle(Figure):
    def __init__(self, coord_a: int, coord_b: int, coord_c: int):
        super().__init__()  # по условию надо будет это писать,так как дочерние от Figure
        self.coord_a = coord_a
        self.coord_b = coord_b
        self.coord_c = coord_c

    def perimeter_triangle(self):
        perimeter = self.coord_a + self.coord_b + self.coord_c
        return perimeter

    def area_triangle(self):
        half_perimeter = (self.coord_a + self.coord_b + self.coord_c) / 2
        area = math.sqrt(half_perimeter * (half_perimeter - self.coord_a) * (half_perimeter - self.coord_b) * (
                half_perimeter - self.coord_c))
        return area


if __name__ == "__main__":
    # Ex.2
    # Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.
    my_list = [Square(2, 3), Circle(2, 3), Triangle(2, 3, 4)]
    for area_figure in my_list:
        if area_figure == my_list[0]:
            print(f"Area of square: {area_figure.area_square()}")
        elif area_figure == my_list[1]:
            print(f"Area of circle: {area_figure.area_circle()}")
        elif area_figure == my_list[2]:
            print(f"Area of triangle: {area_figure.area_triangle()}")
