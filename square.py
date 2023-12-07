import unittest


def area(a):
    """Принимает сторону a и возвращает площадь квадрата с такой стороной
    Параметр: a (int) - сторона квадарата
    Возвращает: area (int) - площадь квадрата с указанной стороной

    print(area(3))
    ---------------------
    9"""
    return a * a


def perimeter(a):
    """Принимает сторону a и возвращает периметр квадарата с таким радиусом
    Параметр: a (int) - сторона квадарата
    Возвращает: perimeter (int) - периметер квадрата с указанной стороной

    print(perimeter(3))
    ---------------------
    12"""
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_area_right(self):
        res = area( )
        self.assertEqual(res, 25)
        res = area(61)
        self.assertEqual(res, 3721)
        res = area(32)
        self.assertEqual(res, 1024)

    def test_perim_right(self):
        res = perimeter(10)
        self.assertEqual(res, 40)
        res = perimeter(6)
        self.assertEqual(res, 24)
        res = perimeter(47)
        self.assertEqual(res, 188)

    def test_area_errors(self):
        with self.assertRaises(TypeError):
            area()
        with self.assertRaises(TypeError):
            area("a")
        with self.assertRaises(TypeError):
            area(0)
        with self.assertRaises(TypeError):
            area(-5)
        with self.assertRaises(TypeError):
            area(5, 7)

    def test_perimeter_errors(self):
        with self.assertRaises(TypeError):
            perimeter()
        with self.assertRaises(TypeError):
            perimeter("a")
        with self.assertRaises(TypeError):
            perimeter(0)
        with self.assertRaises(TypeError):
            perimeter(-3)
        with self.assertRaises(TypeError):
            perimeter(3, 1)