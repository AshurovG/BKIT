from eq import get_roots
import unittest

# Тестируем правильность решения биквадратных уравнений:


class Testing(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.equation1 = get_roots(5, -4, 1)
        self.equation2 = get_roots(1, -5, -36)
        self.equation3 = get_roots(1, -5, 4)
        self.equation4 = get_roots(1, 0, 0)

    def test_area(self):
        self.assertEqual(self.equation1, [])
        self.assertEqual(self.equation2, [-3, 3])
        self.assertEqual(self.equation3, [-2, -1, 1, 2])
        self.assertEqual(self.equation4, [0])


if __name__ == '__main__':
    unittest.main()
