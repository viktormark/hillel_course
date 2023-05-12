# Написать класс для сущности Точка(содержит в себе координаты Х и Y).
# Написать классы для сущностей Треугольник, Квадрат, которые аггрегируют объекты класса Точка.
# Написать методы, которые считают площадь фигур, если координаты введены правильно. Если нет, то показать сообщение об ошибке.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def calculate_area(self):
        if self.validate_coordinates():  # Формула Гаусса
            area = abs((self.point1.x * (self.point2.y - self.point3.y) +
                        self.point2.x * (self.point3.y - self.point1.y) +
                        self.point3.x * (self.point1.y - self.point2.y)) / 2)
            return area
        else:
            return "неправильные координаты треугольника"

    def validate_coordinates(self):
        # Если площадь равна 0, то точки лежат на одной прямой.
        area = abs((self.point1.x * (self.point2.y - self.point3.y) +
                    self.point2.x * (self.point3.y - self.point1.y) +
                    self.point3.x * (self.point1.y - self.point2.y)) / 2)

        if area == 0:
            return False
        else:
            return True


class Square:
    def __init__(self, point1, point2, point3, point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4

    def calculate_area(self):
        side = abs(self.point1.x - self.point2.x)
        area = side ** 2
        return area


point1 = Point(6, 5)
point2 = Point(4, 4)
point3 = Point(3, 5)
point4 = Point(4, 9)

triangle = Triangle(point1, point2, point3)
square = Square(point1, point2, point3, point4)

triangle_area = triangle.calculate_area()
square_area = square.calculate_area()

print(f"Triangle area: {triangle_area}")
print(f"Square area: {square_area}")
