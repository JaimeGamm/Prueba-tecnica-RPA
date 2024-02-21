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
