# ------------------------------------------------------
# EJERCICIO 1 - MAYOR DE EDAD
# ------------------------------------------------------

# Pedimos al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))

# Verificamos si es mayor de 18 años
if edad > 18:
    print("Es mayor de edad.")


# ------------------------------------------------------
# EJERCICIO 2 - APROBADO O DESAPROBADO
# ------------------------------------------------------

# Pedimos al usuario que ingrese su nota
nota = int(input("Ingrese su nota: "))

# Evaluamos si está aprobado o desaprobado
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# ------------------------------------------------------
# EJERCICIO 3 - VERIFICADOR DE NÚMERO PAR
# ------------------------------------------------------

# Pedimos al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Verificamos si el número es par usando el operador módulo
if numero % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")


# ------------------------------------------------------
# EJERCICIO 4 - CATEGORIZACIÓN POR EDAD
# ------------------------------------------------------

# Solicitamos la edad del usuario
edad = int(input("Ingrese su edad: "))

# Evaluamos la categoría según la edad ingresada
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


# ------------------------------------------------------
# EJERCICIO 5 - VALIDACIÓN DE CONTRASEÑA
# ------------------------------------------------------

# Solicitamos al usuario que ingrese una contraseña
contraseña = input("Ingrese una contraseña: ")

# Verificamos que tenga entre 8 y 14 caracteres (inclusive)
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


# ------------------------------------------------------
# EJERCICIO 6 - ANÁLISIS DE SESGO EN DISTRIBUCIÓN
# ------------------------------------------------------

import random
from statistics import mean, median, mode

# Generamos una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculamos media, mediana y moda
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Mostramos los valores calculados
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# Determinamos el tipo de sesgo
if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se detecta un sesgo claro")



# ------------------------------------------------------
# EJERCICIO 7 - AGREGAR SIGNO DE EXCLAMACIÓN SI TERMINA EN VOCAL
# ------------------------------------------------------

# Solicitamos una frase o palabra al usuario
texto = input("Ingrese una frase o palabra: ")

# Verificamos si el texto no está vacío
if len(texto) > 0:
    # Obtenemos el último carácter y lo pasamos a minúscula
    ultima_letra = texto[-1].lower()

    # Si termina en vocal, agregamos el signo de exclamación
    if ultima_letra in ['a', 'e', 'i', 'o', 'u']:
        texto += "!"

# Mostramos el resultado final
print("Resultado:", texto)



# ------------------------------------------------------
# EJERCICIO 8 - TRANSFORMACIÓN DEL NOMBRE SEGÚN OPCIÓN
# ------------------------------------------------------

# Solicitamos el nombre al usuario
nombre = input("Ingrese su nombre: ")

# Solicitamos la opción deseada
print("Seleccione una opción:")
print("1. Mostrar nombre en mayúsculas")
print("2. Mostrar nombre en minúsculas")
print("3. Mostrar nombre con la primera letra en mayúscula")
opcion = input("Ingrese 1, 2 o 3: ")

# Aplicamos la transformación según la opción elegida
if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción no válida.")


# ------------------------------------------------------
# EJERCICIO 9 - CLASIFICACIÓN DE TERREMOTOS SEGÚN MAGNITUD
# ------------------------------------------------------

# Solicitamos la magnitud al usuario
magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Clasificamos según la escala de Richter
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")


# ------------------------------------------------------
# EJERCICIO 10 - DETERMINAR ESTACIÓN SEGÚN HEMISFERIO Y FECHA
# ------------------------------------------------------

# Solicitamos datos al usuario
hemisferio = input("Ingrese su hemisferio (N/S): ").strip().upper()
mes = int(input("Ingrese el número del mes (1 a 12): "))
dia = int(input("Ingrese el día del mes: "))

# Convertimos fecha en formato mes-dia para comparar
fecha = (mes, dia)

# Definimos estaciones para el hemisferio sur
if hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"

# Estaciones para el hemisferio norte (se invierten)
elif hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"
else:
    estacion = "Hemisferio inválido"

# Mostramos el resultado
print("La estación es:", estacion)







