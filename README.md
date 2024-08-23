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

4. Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan dos números enteros,
   correspondientes al total de la compra y al dinero recibido. Informar cuántos billetes de cada denominación deben ser entregados como vuelto, de tal forma que se minimice la cantidad de billetes.
   Considerar que existen billetes $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el dinero recibido fuera insuficiente o si el cambio no
   pudiera entregarse debido a falta de billetes con denominaciones adecuadas.
   Ejemplo: Si la compra es de $3170 y se abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1 billete de $200, 1 billete de $100 y 3 billetes de $10.

5. Escribir funciones lambda para:
   
     a. Informar si un número es oblongo. Se dice que un número es oblongo cuando se puede obtener multiplicando dos números naturales consecutivos.
        Por ejemplo 6 es oblongo porque resulta de multiplicar 2 * 3.
   
     b. Informar si un número es triangular. Un número se define como triangular si puede expresarse como la suma de un grupo de números naturales consecutivos comenzando desde 1.
        Por ejemplo 10 es un número triangular porque se obtiene sumando 1+2+3+4.

    Ambas funciones lambda reciben como único parámetro el número a evaluar y devuelven True o False. No se permite utilizar ayudas externas a las mismas.
   
6. Desarrollar una función que reciba como parámetros dos números enteros positivos y devuelva como valor de retorno el número que resulte de concatenar ambos parámetros.
   Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite utilizar facilidades de Python no vistas en clase.

7. Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros correspondientes el día siguiente al dado.
   Utilizando esta función sin modificaciones ni agregados, desarrollar programas que permitan:

   a. Sumar N días a una fecha.

   b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
   
8. La siguiente función permite averiguar el día de la semana para una fecha determinada. La fecha se suministra en forma de tres parámetros enteros y la función devuelve 0
   para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para imprimir por pantalla el calendario de un mes completo, correspondiente a un mes 
   y año cualquiera basándose en la función suministrada. Considerar que la semana comienza en domingo.

    ![image](https://github.com/user-attachments/assets/db418f3c-4cb1-44c3-a90b-31fd78b517a1)

9. Resolver el siguiente problema utilizando funciones:
    
   Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso para poder cargar los camiones de reparto.
   La empresa cuenta con N camiones, y cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón caben 100 naranjas con un peso de entre 200 y 300 gramos cada una.
   Si el peso de alguna naranja se encuentra fuera del rango indicado se la clasifica para procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas cosechadas e informar cuántos
   cajones se pueden llenar, cuántas naranjas son para jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente reparto.
   Simular el peso de cada unidad generando un número entero al azar entre 150 y 350.

   Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando que la ocupación del camión no debe ser inferior al 80%; en
   caso contrario el camión no serán despachado por su alto costo. 


