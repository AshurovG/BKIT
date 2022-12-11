import fib
import unittest
import time


class TestFib(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(list(fib.Get_Fib_n(0)), [])

    def test_one(self):
        self.assertEqual(list(fib.Get_Fib_n(1)), [1])

    def test_three(self):
        self.assertEqual(list(fib.Get_Fib_n(3)), [1, 1, 2])

    def test_time(self):
        begin = time.time()
        a = fib.Get_Fib_n(200000)
        end = time.time()
        self.assertLess(end - begin, 1)


if __name__ == '__main__':
    unittest.main()
