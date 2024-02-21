import unittest
from unittest.mock import patch
from io import StringIO
from Inventory import Inventory

class TestInventoryMethods(unittest.TestCase):
    
    def test_register_product1(self):
        # Crear una instancia de la clase Inventory
        inventory = Inventory()

        # Mock de datos para la prueba
        grupo = 1
        product = "New Product"
        quantity = 10

        # Llamar a register_product
        inventory.register_product(grupo, product, quantity)

        # Obtener el nuevo estado del inventario después de llamar a register_product
        new_stock = inventory.dairy_stock

        # Verificar que el nuevo producto se haya registrado correctamente
        self.assertIn(product, inventory.dairy_products )
        self.assertEqual(new_stock[-1], quantity)
        
    def test_register_product2(self):
            # Crear una instancia de la clase Inventory
        inventory = Inventory()

        # Mock de datos para la prueba
        grupo = 2
        product = "Limpia vidrios"
        quantity = 80

        # Llamar a register_product
        inventory.register_product(grupo, product, quantity)

        # Obtener el nuevo estado del inventario después de llamar a register_product
        new_stock = inventory.cleaning_stock

        # Verificar que el nuevo producto se haya registrado correctamente
        self.assertIn(product, inventory.cleaning_products )
        self.assertEqual(new_stock[-1], quantity)

    def test_register_product3(self):
            # Crear una instancia de la clase Inventory
        inventory = Inventory()

        # Mock de datos para la prueba
        grupo = 3
        product = "Frijol"
        quantity = 90

        # Llamar a register_product
        inventory.register_product(grupo, product, quantity)

        # Obtener el nuevo estado del inventario después de llamar a register_product
        new_stock = inventory.grain_stock

        # Verificar que el nuevo producto se haya registrado correctamente
        self.assertIn(product, inventory.grain_products)
        self.assertEqual(new_stock[-1], quantity)

    def test_show_inventory(self):
        # Crear una instancia de la clase Inventory
        inventory = Inventory()

        # Redirigir la salida estándar a un objeto StringIO para capturarla
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Llamar a show_inventory
            inventory.show_inventory()

            # Obtener la salida capturada
            output = mock_stdout.getvalue()

        # Verificar si la salida contiene información esperada
        self.assertIn("Inventario:", output)
        self.assertIn("Dairy", output)
        self.assertIn("Cleaning", output)
        self.assertIn("Grain", output)
        
if __name__ == '__main__':
    unittest.main()