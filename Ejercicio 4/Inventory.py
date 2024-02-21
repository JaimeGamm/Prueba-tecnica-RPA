class Inventory:
    MSG_LINEAS_TABLA = "\n---------------------------------"
    MSG_INVALID_GROUP = "Grupo no válido"
    MSG_SELECT = "Selecciono"
    MSG_ENTER_GROUP_NUMBER = "Ingrese el número de grupo (1. dairy 2. cleaning 3. grain): "
    MSG_ERROR_ENTER_NUMBER = "Error: Ingrese un número válido para el grupo."
    MSG_ENTER_QUANTITY = "Ingrese la cantidad: "
    MSG_ERROR_ENTER_VALUE_NUMERICAL="Error: ingrese un valor numerico"
    MSG_MENU = "\nMenú:"
    MSG_SHOW_INVENTORY = "1. Mostrar Inventario"
    MSG_REGISTER_PRODUCT="2. Registrar product"
    MSG_EXIT = "3. Salir"
    MSG_SHOW_NAME_PRODUCT = "Ingrese el nombre del product: "
    MSG_SELECT_OPTION = "Seleccione una opción: "
    MSG_PRODUCT_REGISTERED = "product registrado exitosamente."
    MSG_INVALID_OPTION = "Opción no válida. Intente nuevamente."
    MSG_EXIT2 = "Saliendo del programa. Hasta luego."

    VALUE_ONE = "1"
    VALUE_TWO = "2"
    VALUE_THREE = "3"

    



    def __init__(self):
        self.dairy_products = ["Fairlife Milk", "Alta Dena Milk", "Queensland Butter"]
        self.cleaning_products = ["Detergent", "Bleach", "All-Purpose Cleaner"]
        self.grain_products = ["Rice", "Quinoa", "Oats"]
        self.dairy_stock = [28, 36, 50]
        self.cleaning_stock = [20, 15, 30]
        self.grain_stock = [40, 25, 15]
        self.menu()

    """
        show_inventory()
        Muestra el inventario clasificado por grupos con products y existencias.
    """
    def show_inventory(self):
        print("Inventario:")
        self.print_group("Dairy", self.dairy_products, self.dairy_stock)
        self.print_group("Cleaning", self.cleaning_products, self.cleaning_stock)
        self.print_group("Grain", self.grain_products, self.grain_stock)

    """
        print_group()
        imprimer products y existencias de un grupo específico.
        :param grupo: Nombre del grupo.
        :param products: Lista de nombres de products.
        :param existencias: Lista de quantityes de existencias.
    """
    def print_group(self, grupo, products, existencias):
        print(self.MSG_LINEAS_TABLA)
        print("\nGrupo: {}".format(grupo))
        print(self.MSG_LINEAS_TABLA)
        print("{:<20} {:<10}".format("product", "Existencias"))
        for product, existencia in zip(products, existencias):
            print("{:<20} {:<10}".format(product, existencia))

    """
        register_product()
        Registra un producto en un grupo específico o actualiza la cantidad existente. Si se va a actualizar la cantidad del producto, en el caso de disminuir la cantidad, ingrese el nombre del producto y luego ingrese la cantidad a disminuir con un signo negativo.
    """  
    def register_product(self, grupo, product, quantity):
     
        if grupo == 1:
            self.register_in_group(product, quantity, self.dairy_products, self.dairy_stock)
            self.new_record_message("Dairy", self.dairy_products[-1], self.dairy_stock[-1])

        elif grupo == 2:
            self.register_in_group(product, quantity, self.cleaning_products, self.cleaning_stock)
            self.new_record_message("Cleaning", self.cleaning_products[-1], self.cleaning_stock[-1])

        elif grupo == 3:
            self.register_in_group(product, quantity, self.grain_products, self.grain_stock)
            self.new_record_message("grain", self.grain_products[-1], self.grain_stock[-1])
        else:
            print(self.MSG_INVALID_GROUP)


    """
        register_in_group()
        Registra un producto en un grupo específico o actualiza la cantidad existente.

    """
    def register_in_group(self, product, quantity, products, existencias):
        if product in products:
            indice = products.index(product)
            existencias[indice] += quantity
        else:
            products.append(product)
            existencias.append(quantity)
    
    def new_record_message(self, grupo, product, quantity):
        print(self.MSG_LINEAS_TABLA)
        print(f"Se ha registrado {grupo} {product} {quantity}")
    
    def message_select(self,opcion):
        print(self.MSG_LINEAS_TABLA)
        print(self.MSG_SELECT + opcion)
        print(self.MSG_LINEAS_TABLA)
    
    """
    Asignar el grupo en el menú a la hora de registrar un producto.
    """
    def choose_group_menu(self):
        grupo = 0
        try:
            grupo = int(input(self.MSG_ENTER_GROUP_NUMBER))
            if grupo > 3:
                print(self.MSG_ERROR_ENTER_NUMBER)
                grupo = self.choose_group_menu()
        except (ValueError) :
            print(self.MSG_ERROR_ENTER_NUMBER)
            grupo = self.choose_group_menu()
        return grupo    
        
    """
        Solicita al usuario ingresar la cantidad del producto y maneja posibles errores.
        :return: Cantidad del producto ingresada por el usuario.
    """    
    def enter_quantity_product(self):
        quantity = 0
        try:
            quantity = int(input(self.MSG_ENTER_QUANTITY))
        except (ValueError):
             print(self.MSG_ERROR_ENTER_VALUE_NUMERICAL)
             quantity= self.enter_quantity_product()
        return quantity 
    
    def menu(self):
        while True:
            print(self.MSG_MENU)
            print(self.MSG_SHOW_INVENTORY)
            print(self.MSG_REGISTER_PRODUCT)
            print(self.MSG_EXIT)

            opcion = input(self.MSG_SELECT_OPTION)

            if opcion == self.VALUE_ONE:
                self.message_select(self.MSG_SHOW_INVENTORY)
                self.show_inventory()
            elif opcion == self.VALUE_TWO:
                self.message_select(self.MSG_REGISTER_PRODUCT)
                grupo =self.choose_group_menu()
                product = input(self.MSG_SHOW_NAME_PRODUCT)
                quantity = self.enter_quantity_product()
                self.register_product(grupo, product, quantity)
                print(self.MSG_PRODUCT_REGISTERED)
            elif opcion == self.VALUE_THREE:
                self.message_select(self.MSG_EXIT)
                print(self.MSG_EXIT2)
                break
            else:
                print(self.MSG_INVALID_OPTION)


if __name__ == "__main__":
    inventario = Inventory()
