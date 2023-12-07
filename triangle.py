import unittest


def area(a, h):
    """Принимает основание a и высоту h треугольника и возвращает площадь 
    такого треугольника
    Параметры: a (int) - основание треугольника
               h (int) - высота треугольника
    Возвращает: area (int) - площадь треугольника с указанными параметрами

    print(area(3, 2))
    ---------------------
    3"""
    return a * h / 2


def perimeter(a, b, c):
    """Принимает стороны a, b, c треугольника и возвращает периметр такого 
    треугольника
    Параметры: a (int) - первая сторона
               b (int) - вторая сторона
               c (int) - третья сторона
    Возвращает: perimeter (int) - периметр треугольника с указанными сторонами

    print(perimeter(3, 2, 3))
    ---------------------
    8"""
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_area_right(self):
        res = area(5, 7)
        self.assertEqual(res, 17.5)
        res = area(7, 5)
        self.assertEqual(res, 17.5)
        res = area(10, 6)
        self.assertEqual(res, 30)
        res = area(6, 10)
        self.assertEqual(res, 30)

    def test_perim_right(self):
        res = perimeter(8, 10, 6)
        self.assertEqual(res, 24)
        res = perimeter(47, 61, 54)
        self.assertEqual(res, 162)
        res = perimeter(54, 47, 61)
        self.assertEqual(res, 162)
        res = perimeter(32, 32, 32)
        self.assertEqual(res, 96)

    def test_area_errors(self):
        with self.assertRaises(TypeError):
            area(1)
        with self.assertRaises(TypeError):
            area("a", 1)
        with self.assertRaises(TypeError):
            area("a", "b")
        with self.assertRaises(TypeError):
            area(0, 5)
        with self.assertRaises(TypeError):
            area(7, 0)
        with self.assertRaises(TypeError):
            area(0, 0)
        with self.assertRaises(TypeError):
            area(-5, 5)
        with self.assertRaises(TypeError):
            area(5, -7)
        with self.assertRaises(TypeError):
            area(-5, -7)
        with self.assertRaises(TypeError):
            area(-5, -7, 8)

    def test_perimeter_errors(self):
        with self.assertRaises(TypeError):
            perimeter(1, 2)
        with self.assertRaises(TypeError):
            perimeter("a", 1, 2)
        with self.assertRaises(TypeError):
            perimeter("a", "b", 2)
        with self.assertRaises(TypeError):
            perimeter("a", "b", "c")
        with self.assertRaises(TypeError):
            perimeter(0, 1, 2)
        with self.assertRaises(TypeError):
            perimeter(0, 0, 2)
        with self.assertRaises(TypeError):
            perimeter(0, 0, 0)
        with self.assertRaises(TypeError):
            perimeter(-3, 1, 2)
        with self.assertRaises(TypeError):
            perimeter(-3, -1, 2)
        with self.assertRaises(TypeError):
            perimeter(-3, -1, -2)
        with self.assertRaises(TypeError):
            perimeter(-3, -1, -2)
        with self.assertRaises(TypeError):
            perimeter(-3, -1, -2, 0)