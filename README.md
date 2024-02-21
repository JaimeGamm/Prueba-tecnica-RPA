<h1>Prueba técnica RPA</h1>
<p>
  Cada ejercicio está programado en Python y cuenta con sus respectivos tests para garantizar su correcto funcionamiento.
</p>

<h2>Ejercicio 1.</h2>

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
