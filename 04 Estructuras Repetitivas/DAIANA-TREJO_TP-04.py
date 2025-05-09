# ---------------------------------------------------------------
# Trabajo Práctico 4 - Estructuras Repetitivas
# Ejercicio 1
# ---------------------------------------------------------------

# Crea un programa que imprima en pantalla todos los números 
# enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden 
# creciente, mostrando un número por línea.

# Usamos un bucle for para recorrer del 0 al 100 inclusive
for numero in range(0, 101):
    print(numero)  # Mostramos cada número en una línea



# ---------------------------------------------------------------
# Trabajo Práctico 4 - Estructuras Repetitivas
# Ejercicio 2
# ---------------------------------------------------------------

# Desarrolla un programa que solicite al usuario un número entero 
# y determine la cantidad de dígitos que contiene.

# Pedimos al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Convertimos el número a positivo en caso de que sea negativo
numero_absoluto = abs(numero)

# Inicializamos el contador de dígitos
cantidad_digitos = 0

# Si el número es 0, tiene 1 solo dígito
if numero_absoluto == 0:
    cantidad_digitos = 1
else:
    # Contamos los dígitos usando un bucle while
    while numero_absoluto > 0:
        numero_absoluto //= 10  # Eliminamos el último dígito
        cantidad_digitos += 1   # Aumentamos el contador

# Mostramos el resultado
print("El número ingresado tiene", cantidad_digitos, "dígito(s).")



# ---------------------------------------------------------------
# Trabajo Práctico 4 - Estructuras Repetitivas
# Ejercicio 3
# ---------------------------------------------------------------

# Escribe un programa que sume todos los números enteros 
# comprendidos entre dos valores dados por el usuario, 
# excluyendo esos dos valores.

# Pedimos al usuario que ingrese los dos valores
inicio = int(input("Ingrese el primer valor: "))
fin = int(input("Ingrese el segundo valor: "))

# Aseguramos que inicio sea menor que fin, si no lo está, los intercambiamos
if inicio > fin:
    inicio, fin = fin, inicio

# Inicializamos la suma acumulada
suma = 0

# Recorremos los números entre los dos valores (excluyendo ambos)
for numero in range(inicio + 1, fin):
    suma += numero  # Sumamos cada número al total

# Mostramos el resultado
print("La suma de los números entre", inicio, "y", fin, "es:", suma)



# ---------------------------------------------------------------
# Trabajo Práctico 4 - Estructuras Repetitivas
# Ejercicio 4
# ---------------------------------------------------------------

# Elabora un programa que permita al usuario ingresar números 
# enteros y los sume en secuencia. El programa debe detenerse y 
# mostrar el total acumulado cuando el usuario ingrese un 0.

# Inicializamos el acumulador
suma = 0

# Bucle infinito hasta que el usuario ingrese 0
while True:
    numero = int(input("Ingrese un número entero (0 para finalizar): "))
    if numero == 0:
        break  # Si el número es 0, salimos del bucle
    suma += numero  # Sumamos el número al total

# Mostramos el total acumulado
print("La suma total es:", suma)




# ---------------------------------------------------------------
# Trabajo Práctico 4 - Estructuras Repetitivas
# Ejercicio 5
# ---------------------------------------------------------------

# Crea un juego en el que el usuario deba adivinar un número 
# aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos 
# intentos fueron necesarios para acertar el número.

import random  # Importamos el módulo para generar números aleatorios

# Generamos un número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)

# Inicializamos el contador de intentos
intentos = 0

# Bucle hasta que el usuario adivine el número
while True:
    adivinanza = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1  # Sumamos un intento
    if adivinanza == numero_secreto:
        print("¡Correcto! Adivinaste el número en", intentos, "intento(s).")
        break
    else:
        print("Incorrecto, intentá de nuevo.")



# ---------------------------------------------------------------
# Trabajo Práctico 4 - Estructuras Repetitivas
# Ejercicio 6
# ---------------------------------------------------------------

# Desarrolla un programa que imprima en pantalla todos los 
# números pares comprendidos entre 0 y 100, en orden decreciente.

# Recorremos desde 100 hasta 0, de 2 en 2 hacia atrás
for numero in range(100, -1, -2):
    print(numero)



# ---------------------------------------------------------------
# Trabajo Práctico 4 - Estructuras Repetitivas
# Ejercicio 7
# ---------------------------------------------------------------

# Crea un programa que calcule la suma de todos los números 
# comprendidos entre 0 y un número entero positivo indicado por el usuario.

# Solicitamos un número entero positivo
limite = int(input("Ingrese un número entero positivo: "))

# Validamos que el número sea positivo
while limite < 0:
    limite = int(input("Por favor ingrese un número POSITIVO: "))

# Inicializamos el acumulador
suma = 0

# Recorremos del 0 al número ingresado (inclusive)
for numero in range(0, limite + 1):
    suma += numero

# Mostramos el resultado
print("La suma de los números entre 0 y", limite, "es:", suma)




# ---------------------------------------------------------------
# Trabajo Práctico 4 - Estructuras Repetitivas
# Ejercicio 8
# ---------------------------------------------------------------

# Escribe un programa que permita al usuario ingresar 100 números 
# enteros. Luego, el programa debe indicar cuántos de estos números 
# son pares, cuántos son impares, cuántos son negativos y cuántos 
# son positivos. (Nota: para probar el programa puedes usar una 
# cantidad menor, pero debe estar preparado para procesar 100 
# números con un solo cambio).

# Definimos la cantidad de números que se van a ingresar
CANTIDAD = 100  # Cambiar a un número menor para pruebas si es necesario

# Inicializamos contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Ingresamos los números uno por uno
for i in range(CANTIDAD):
    numero = int(input(f"Ingrese el número {i+1}: "))

    # Verificamos si es par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Verificamos si es positivo o negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

# Mostramos los resultados
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)




# ---------------------------------------------------------------
# Trabajo Práctico 4 - Estructuras Repetitivas
# Ejercicio 9
# ---------------------------------------------------------------

# Elabora un programa que permita al usuario ingresar 100 números 
# enteros y luego calcule la media de esos valores. (Nota: puedes 
# probar el programa con una cantidad menor, pero debe poder procesar 
# 100 números cambiando solo un valor).

# Definimos la cantidad total de números a ingresar
CANTIDAD = 10  # Cambiar a un valor menor para hacer pruebas si se desea

# Inicializamos el acumulador
suma = 0

# Ingresamos los números uno por uno y los vamos sumando
for i in range(CANTIDAD):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero

# Calculamos la media
media = suma / CANTIDAD

# Mostramos el resultado
print("La media de los", CANTIDAD, "números es:", media)




# ---------------------------------------------------------------
# Trabajo Práctico 4 - Estructuras Repetitivas
# Ejercicio 10
# ---------------------------------------------------------------

# Escribe un programa que invierta el orden de los dígitos de un 
# número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, 
# el programa debe mostrar 745.

# Pedimos al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Inicializamos la variable para guardar el número invertido
numero_invertido = 0

# Guardamos el signo original
es_negativo = numero < 0

# Trabajamos con el valor absoluto del número
numero = abs(numero)

# Bucle para invertir los dígitos
while numero > 0:
    digito = numero % 10  # Obtenemos el último dígito
    numero_invertido = numero_invertido * 10 + digito  # Lo agregamos al invertido
    numero //= 10  # Quitamos el último dígito del número original

# Si el número era negativo, lo convertimos nuevamente
if es_negativo:
    numero_invertido = -numero_invertido

# Mostramos el resultado
print("El número invertido es:", numero_invertido)









