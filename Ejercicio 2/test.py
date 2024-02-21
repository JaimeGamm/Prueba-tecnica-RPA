import unittest
from procesar_numeros import process_numbers


class TestProcessNumbers(unittest.TestCase):
    
    def test_case1(self):
        entrada = [24, 150, 300, 660, 295, 1050, 50]
        result_esperado = [150, 300, 295]
        self.assertEqual(process_numbers(entrada), result_esperado)

    def test_case2(self):
        entrada = [110, 720, 307, 555, 1095, 12, 300, 1000]
        result_esperado = [110, 555]
        self.assertEqual(process_numbers(entrada), result_esperado)

    def test_case3(self):
        entrada = [45, 670, 880, 1200, 200, 990]
        result_esperado = [45]
        self.assertEqual(process_numbers(entrada), result_esperado)

    def test_case4(self):
        entrada = [800, 900, 1100, 1200, 1300]
        result_esperado = []
        self.assertEqual(process_numbers(entrada), result_esperado)

    def test_case5(self):
        entrada = []
        result_esperado = []
        self.assertEqual(process_numbers(entrada), result_esperado)

if __name__ == '__main__':
    unittest.main()