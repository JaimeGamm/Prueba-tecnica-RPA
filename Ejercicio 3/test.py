import unittest
from group_items import group_items

class TestGroupItems(unittest.TestCase):
    
    def test_case1(self):
        entrada = [12, 25, 1, 1, 7, 25]
        resultado_esperado = [[12], [25, 25], [1, 1], [7]]
        self.assertEqual(group_items(entrada), resultado_esperado)

    def test_case2(self):
        entrada = [6, 7, 8, 9]
        resultado_esperado = [[6], [7], [8], [9]]
        self.assertEqual(group_items(entrada), resultado_esperado)

    def test_case3(self):
        entrada = [1, 1, 1, 1]
        resultado_esperado = [[1, 1, 1, 1]]
        self.assertEqual(group_items(entrada), resultado_esperado)

    def test_case4(self):
        entrada = []
        resultado_esperado = []
        self.assertEqual(group_items(entrada), resultado_esperado)

if __name__ == '__main__':
    unittest.main()