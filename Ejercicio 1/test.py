import unittest
from sum_series import sum_serie



class TestSumSerie(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_serie(3, 5), 37035)

    def test_2(self):
        self.assertEqual(sum_serie(5, 3), 615)

    def test_3(self):
        self.assertEqual(sum_serie(2, 0), 0)

    def test_4(self):
        self.assertEqual(sum_serie(7, 1), 7)

    def test_5(self):
        self.assertEqual(sum_serie(0, 8), 0)

    def test_6(self):
        self.assertEqual(sum_serie(-2, 3), -246)


if __name__ == '__main__':
    unittest.main()