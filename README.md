<h1>Prueba técnica RPA</h1>
<p>
  Cada ejercicio está programado en Python y cuenta con sus respectivos tests para garantizar su correcto funcionamiento.
</p>

<h2>Ejercicio 1.</h2>
<h3>Escriba una función que retorne la suma de una serie de X número repetido hasta el n-ésimo término.</h3>

<p>
  Para ejecutar el archivo del ejercicio 1, abrimos una terminal y nos dirigimos a la ruta donde se encuentra el archivo, luego ejecutamos el siguiente comando:
  
</p>
<p align="center">
  <strong>python sum_series.py</strong>
</p>
<p>
  En el ejercicio 1, el programa viene configurado para imprimir los ejemplos que se presentaron en el taller. Sin embargo, es posible personalizar las entradas modificando la línea de código <strong>'print(sum_serie(number, terms))'</strong> para obtener resultados específicos según las preferencias del usuario.
</p>
<p>
  El test de este ejercicio comprende seis casos de prueba.
</p>
<table align="center">
  <thead>
    <tr>
      <th>Número de Caso</th>
      <th>Entrada numero</th>
      <th>Entrada terminos</th>
      <th>Salida Resultado</th>
    </tr>
  </thead>
  <tbody align="center">
    <tr>
      <td>1</td>
      <td>3</td>
      <td>5</td>
      <td>37035</td>
    </tr>
    <tr>
      <td>2</td>
      <td>5</td>
      <td>3</td>
      <td>615</td>
    </tr>
    <tr>
      <td>3</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>7</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <td>5</td>
      <td>0</td>
      <td>8</td>
      <td>0</td>
    </tr>
    <tr>
      <td>6</td>
      <td>-2</td>
      <td>3</td>
      <td>-246</td>
    </tr>
    <!-- Agrega más filas según sea necesario -->
  </tbody>
</table>
<p>
  Para ejercutar el test en la terminar escribimos el siguiente comando:
</p>
<p align="center">
  <strong>python -m unittest test.py</strong>
</p>
<p>
  Después de ejecutar el test, si todos los casos de prueba son exitosos, la consola mostrará el número total de pruebas que han pasado y el mensaje 'OK', indicando que   la implementación ha superado todas las pruebas con éxito
</p>
<h2>Ejercicio 2.</h2>
<h3>Escriba una función que retorne en una lista de salida, solo aquellos números de una lista de entrada que satisfagan las
siguientes condiciones:

</h3>
<h4 align="center">
1. El número debe ser divisible por cinco. <br>
2. Si el número es mayor que 600, no se incluye en la salida.<br>
3. Si el número es mayor que 1000, detenga el procesamiento y retorne el resultado.<br>  
</h4>
<p>
  Para ejecutar el archivo del ejercicio 2, abrimos una terminal y nos dirigimos a la ruta donde se encuentra el archivo, luego ejecutamos el siguiente comando: 
</p>
<p align="center">
  <strong>python procesar_numeros.py</strong>
</p>

<p>
El ejercicio 2 está configurado inicialmente para imprimir los ejemplos proporcionados en el taller. Sin embargo, brinda la flexibilidad de modificar las entradas directamente mediante la modificación de listas, o llamando al método process_numbers(lista) para procesar una lista específica.
</p>

<p>El test de este ejercicio comprende cinco casos de prueba</p>

<table align="center">
  <thead>
    <tr>
      <th>Número de Caso</th>
      <th>Entrada lista</th>
      <th>resultado esperado</th>
    </tr>
  </thead>
  <tbody align="center">
    <tr>
      <td>1</td>
      <td>[24, 150, 300, 660, 295, 1050, 50]</td>
      <td>[150, 300, 295]</td>
    </tr>
    <tr>
      <td>2</td>
      <td>[110, 720, 307, 555, 1095, 12, 300, 1000]</td>
      <td>[110, 555]</td>
    </tr>
    <tr>
      <td>3</td>
      <td>[45, 670, 880, 1200, 200, 990]</td>
      <td>[45]</td>
    </tr>
    <tr>
      <td>4</td>
      <td>[800, 900, 1100, 1200, 1300]</td>
      <td>[]</td>
    </tr>
    <tr>
      <td>5</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <!-- Agrega más filas según sea necesario -->
  </tbody>
</table>
<p>
  Para ejercutar el test en la terminar escribimos el siguiente comando:
</p>
<p align="center">
  <strong>python -m unittest test.py</strong>
</p>
<h2>Ejercicio 3.</h2>
<h3>
  Dada una lista de cualquier longitud de entrada, escriba una función para agrupar los elementos similares en una matriz
  de salida (no importa el orden).
</h3>
<p>
  Para ejecutar el archivo del ejercicio 3, abrimos una terminal y nos dirigimos a la ruta donde se encuentra el archivo, luego ejecutamos el siguiente comando: 
</p>
<p align="center">
  <strong>python group_items.py</strong>
</p>
<p>
  El ejercicio 3 está configurado inicialmente para imprimir los ejemplos proporcionados en el taller. Sin embargo, brinda la flexibilidad de modificar las entradas directamente mediante la modificación de listas, o llamando al método group_items(lista) para procesar una lista específica.
</p>
<p>El test de este ejercicio comprende cuatro casos de prueba</p>
<table align="center">
  <thead>
    <tr>
      <th>Número de Caso</th>
      <th>Entrada lista</th>
      <th>resultado esperado</th>
    </tr>
  </thead>
  <tbody align="center">
    <tr>
      <td>1</td>
      <td>[12, 25, 1, 1, 7, 25]</td>
      <td>[[12], [25, 25], [1, 1], [7]]</td>
    </tr>
    <tr>
      <td>2</td>
      <td>[6, 7, 8, 9]</td>
      <td>[[6], [7], [8], [9]]</td>
    </tr>
    <tr>
      <td>3</td>
      <td>[1, 1, 1, 1]</td>
      <td>[[1, 1, 1, 1]]</td>
    </tr>
    <tr>
      <td>4</td>
      <td>[]</td>
      <td>[]</td>
    </tr>
    <!-- Agrega más filas según sea necesario -->
  </tbody>
</table>
<p>
  Para ejercutar el test en la terminar escribimos el siguiente comando:
</p>
<p align="center">
  <strong>python -m unittest test.py</strong>
</p>
<h2>Ejercicio 4.</h2>
<h3>
En un negocio reciben periódicamente productos para la venta, se requiere desarrollar un programa de consola (o
terminal) que cumpla con los siguientes requerimientos:
</h3>

<p>
1. Se requiere organizar el inventario en los siguientes grupos: dairy, cleaning y grain.<br>
2. Cada grupo tiene que estar asociado a un elemento de otra lista que almacena las existencias de ese grupo en la
misma posición, como en el siguiente ejemplo:<br>
dairy_products = [“Fairlife Milk”, “Alta Dena Milk”, “Queensland Butter”]<br>
dairy_stock = [28, 36, 50]<br>
En donde, por ejemplo, el producto del grupo dairy “Alta Dena Milk” tiene una existencia de 36 unidades.
3. Para un producto entrante, se debe poder registrar en el sistema: el nombre del producto, la cantidad y el grupo
al que pertenece.<br>
4. Si el producto no existe en la lista, se debe agregar al final con su cantidad entrante, pero si existe se debe
actualizar el número de existencias sumando la nueva cantidad.<br>
5. El programa debe permitir visualizar todo el inventario de productos y existencias.<br>
<p>

<p>Para ejecutar el archivo del ejercicio 4, abrimos una terminal y nos dirigimos a la ruta donde se encuentra el archivo, luego ejecutamos el siguiente comando:</p>

<p align="center">
  <strong>python Inventory.py</strong>
</p>
<p>
  El ejercicio 4, por defecto, viene cargado con un inventario predefinido. Este inventario inicial incluye productos agrupados en categorías como productos lácteos, productos de limpieza y productos de grano, junto con sus respectivas cantidades disponibles. 
</p>
<p>El test de este ejercicio comprende tres casos de prueba: </p>

<table align="center">
  <thead>
    <tr>
      <th>Caso</th>
      <th>Entrada</th>
      <th>resultado esperado</th>
    </tr>
  </thead>
  <tbody align="center">
    <tr>
      <td>test registar producto 1</td>
      <td>register_product(1, "New Product", 10)</td>
      <td>Se espera que los datos ingresados esten en las listas dairy_products y dairy_stock</td>
    </tr>
    <tr>
      <td>test registar producto 2</td>
      <td>register_product(2, "Limpia vidrios", 80)</td>
      <td>Se espera que los datos ingresados esten en las listas cleaning_products y cleaning_stock</td>
    </tr>
    <tr>
      <td>test registar producto 3</td>
      <td>register_product(3, "Frijol", 90)</td>
      <td>Se espera que los datos ingresados esten en las listas grain_stock y grain_products</td>
    </tr>
    <!-- Agrega más filas según sea necesario -->
  </tbody>
</table>
<p>
  Para ejecutar con éxito las pruebas unitarias del programa, es necesario comentar la llamada al método menu() en la función __init__(self) de la clase Inventory. Una vez realizada esta modificación, se puede proceder a ejecutar las pruebas desde la terminal mediante el siguiente comando.
</p>
<p align="center">
  <strong>python -m unittest test_inventory.py</strong>
</p>
