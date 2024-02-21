def group_items(list_elements):
    result = []
    elements_views = set()

    for element in list_elements:
        if element not in elements_views:
            group_e = [e for e in list_elements if e == element]
            elements_views.add(element)
            result.append(group_e)

    return result

# Ejemplos de uso:
entrada1 = [12, 25, 1, 1, 7, 25]
salida1 = group_items(entrada1)
print("Entrada:", entrada1)
print("Salida:", salida1)

entrada2 = [6, 7, 8, 9]
salida2 = group_items(entrada2)
print("Entrada:", entrada2)
print("Salida:", salida2)
