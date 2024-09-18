# Algoritmos y Estructuras de Datos I - Trabajos Practicos

## TP.1

1. Desarrollar una función que reciba tres números enteros positivos y devuelva el mayor de los tres, sólo si éste es único (es decir el mayor estricto).
   Devolver -1 en caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar también un programa para ingresar los tres valores, invocar a la función y mostrar
   el máximo hallado, o un mensaje informativo si éste no existe.

2. Desarrollar una función que reciba tres números enteros positivos correspondientes al día, mes, año de una fecha y verifique si corresponden a una fecha válida.
   Debe tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos. Devolver True o False según la fecha sea correcta o no.
   Realizar también un programa para verificar el comportamiento de la función.

3. Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un esquema de
   tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar una función que reciba como parámetro la cantidad de viajes realizados en un determinado
   mes y devuelva el total gastado en viajes. Realizar también un programa para verificar el comportamiento de la función.

      ![image](https://github.com/user-attachments/assets/65a34063-566e-4b77-bb30-89545835fb9a)

4. Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan dos números           enteros, correspondientes al total de la compra y al dinero recibido. Informar cuántos billetes de cada denominación deben ser entregados como vuelto, de tal forma que se minimice la     cantidad de billetes.
   Considerar que existen billetes $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el dinero recibido fuera insuficiente o si el cambio no
   pudiera entregarse debido a falta de billetes con denominaciones adecuadas.
   Ejemplo: Si la compra es de $3170 y se abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1 billete de $200, 1 billete de $100 y 3 billetes de $10.

5. Escribir funciones lambda para:
   
     a. Informar si un número es oblongo. Se dice que un número es oblongo cuando se puede obtener multiplicando dos números naturales consecutivos.
        Por ejemplo 6 es oblongo porque resulta de multiplicar 2 * 3.
   
     b. Informar si un número es triangular. Un número se define como triangular si puede expresarse como la suma de un grupo de números naturales consecutivos comenzando desde 1.
        Por ejemplo 10 es un número triangular porque se obtiene sumando 1+2+3+4.

    Ambas funciones lambda reciben como único parámetro el número a evaluar y devuelven True o False. No se permite utilizar ayudas externas a las mismas.
   
7. Desarrollar una función que reciba como parámetros dos números enteros positivos y devuelva como valor de retorno el número que resulte de concatenar ambos parámetros.
   Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades de Python no vistas en clase.

8. Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros correspondientes el      día siguiente al dado. Utilizando esta función sin modificaciones ni agregados, desarrollar programas que permitan:

   a. Sumar N días a una fecha.
   
   b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
   
9. La siguiente función permite averiguar el día de la semana para una fecha determinada. La fecha se suministra en forma de tres parámetros enteros y la función devuelve 0
   para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para imprimir por pantalla el calendario de un mes completo, correspondiente a un mes 
   y año cualquiera basándose en la función suministrada. Considerar que la semana comienza en domingo.

    ![image](https://github.com/user-attachments/assets/db418f3c-4cb1-44c3-a90b-31fd78b517a1)

10. Resolver el siguiente problema utilizando funciones:
    
   Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso para poder cargar los camiones de reparto.
   La empresa cuenta con N camiones, y cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón caben 100 naranjas con un peso de entre 200 y 300 gramos cada una.
   Si el peso de alguna naranja se encuentra fuera del rango indicado se la clasifica para procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas cosechadas e    informar cuántos cajones se pueden llenar, cuántas naranjas son para jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente reparto.
   Simular el peso de cada unidad generando un número entero al azar entre 150 y 350.

   Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando que la ocupación del camión no debe ser inferior al 80%; en
   caso contrario el camión no serán despachado por su alto costo.


## TP.2

1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:

   a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.
   
   b. Calcular y devolver el producto de todos los elementos de la lista anterior.
   
   c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar 
      listas auxiliares.
   
   d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50]

3. Escribir funciones para:

   a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa a través del teclado.
   
   b. Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido. La función no debe modificar la lista.
   
   c. Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de la lista original, sin importar el orden.

5. Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista.

6. Eliminar de una lista de números enteros aquellos valores que se encuentren en una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista resultante.
   La función debe modificar la lista original sin crear una copia modificada.

7. Escribir una función que reciba una lista como parámetro y devuelva True si la lista  está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
   ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar  demás un programa para verificar el comportamiento de la función.

8. Escribir una función que reciba una lista de números enteros como parámetro y la normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones relativas        que cada elemento tiene en la lista original. Desarrollar también un programa que permita verificar el comportamiento de la función. Por ejemplo,
   normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50]

9. Intercalar los elementos de una lista entre los elementos de otra. La intercalación deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará 
   una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3] y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden 
   tener distintas longitudes.

10. Utilizar la técnica de listas por comprensión para construir una lista con todos los números impares comprendidos entre 100 y 200.

11. Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7 que no sean múltiplos de 5. A y B se ingresar desde el teclado.

12. Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los elementos de la primera que sean impares. El proceso deberá realizarse utilizando la función          filter(). Imprimir las dos listas por pantalla. 



