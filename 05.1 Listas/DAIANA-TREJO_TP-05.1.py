
#########

import math
def imprimir_hola_mundo():
    print("Hola Mundo!")

def saludar_usuario(nombre):
    print(f"Hola, {nombre}!")

def informacion_personal(nombre, apellido, edad, residencia):    
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def calcular_area_circulo(radio):
    pi = math.pi
    area = pi * (radio ** 2)
    print(f"El área del círculo con radio {radio} es: {area}")

def calcular_perimetro_circulo(radio):
    pi = math.pi
    perimetro = 2 * pi * radio
    print(f"El perímetro del círculo con radio {radio} es: {perimetro}")

def segundos_a_horas(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    print(f"{segundos} segundos son {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
    print(f"Suma [{a}+{b}]: {suma}")
    print(f"Resta [{a}-{b}]: {resta}")
    print(f"Multiplicación [{a}*{b}]: {multiplicacion}")
    print(f"División [{a}/{b}]: {division}")
    return (suma, resta, multiplicacion, division)

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Tu IMC es: {imc:.2f}")
    if imc < 18.5:
        print("Bajo peso")
    elif 18.5 <= imc < 24.9:
        print("Peso normal")
    elif 25 <= imc < 29.9:
        print("Sobrepeso")
    else:
        print("Obesidad")

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio de {a}, {b} y {c} es: {promedio}")
    
print("Trabajo Práctico 5")
print("Nombre: Trejo, Daiana")
print("Eliga que ejercicio desea ejecutar")
print("1) Ejercicio 1")
print("2) Ejercicio 2")
print("3) Ejercicio 3")
print("4) Ejercicio 4")
print("5) Ejercicio 5")
print("6) Ejercicio 6")
print("7) Ejercicio 7")
print("8) Ejercicio 8")
print("9) Ejercicio 9")
print("10) Ejercicio 10")
print("11) Todos")
print("12) Salir")



opcion = int(input("Ingrese su opción: "))
if opcion == 1 or opcion == 11:
    ## Ejercicio 1    
    print("Ejercicio 1")
    print(f""" Crear una función llamada imprimir_hola_mundo que imprima por
    pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
    programa principal. """)
    
    print("Llamando a la función imprimir_hola_mundo()")
    imprimir_hola_mundo()
    print("Llamada a la función finalizada")

    print("Fin Ejercicio 1\n")

if opcion == 2 or opcion == 11:
    ## Ejercicio 2
    print("Ejercicio 2")
    print(f""" 2. Crear una función llamada saludar_usuario(nombre) que reciba
    como parámetro un nombre y devuelva un saludo personalizado.
    Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
    volver: “Hola Marcos!”. Llamar a esta función desde el programa
    principal solicitando el nombre al usuario. """)
    
    print("Llamando a la función saludar_usuario()")
    nombre = input("Ingrese su nombre: ")
    saludar_usuario(nombre)
    print("Llamada a la función finalizada")
    
    print("Fin Ejercicio 2\n")

if opcion == 3 or opcion == 11:
    ## Ejercicio 3
    print("Ejercicio 3")
    print(f"""3. Crear una función llamada informacion_personal(nombre, apellido,
    edad, residencia) que reciba cuatro parámetros e imprima: “Soy
    [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
    dir los datos al usuario y llamar a esta función con los valores in-
    gresados.""")

    edad_correcta = False
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    while not edad_correcta:
        edad = int(input("Ingrese su edad: "))
        if edad < 0:
            print("La edad no puede ser negativa. Intente nuevamente.")
        else:
            edad_correcta = True
    residencia = input("Ingrese su residencia: ")
    print("Llamando a la función informacion_personal()")
    informacion_personal(nombre, apellido, edad, residencia)
    print("Llamada a la función finalizada")

    
    
    print("Fin Ejercicio 3\n")

if opcion == 4 or opcion == 11:
    ## Ejercicio 4
    print("Ejercicio 4")
    print(f"""4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
    dio como parámetro y devuelva el área del círculo. calcular_peri-
    metro_circulo(radio) que reciba el radio como parámetro y devuel-
    va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
    bas funciones para mostrar los resultados.""")
    radio_correcto = False
    while not radio_correcto:
        radio = float(input("Ingrese el radio del círculo: "))
        if radio < 0:
            print("El radio no puede ser negativo. Intente nuevamente.")
        else:
            radio_correcto = True
    print("Llamando a la función calcular_area_circulo()")
    calcular_area_circulo(radio)
    print("Llamada a la función calcular_area_circulo() finalizada")
    print("Llamando a la función calcular_perimetro_circulo()")
    calcular_perimetro_circulo(radio)
    print("Llamada a la función calcular_perimetro_circulo() finalizada")        
    print("Fin Ejercicio 4\n")

if opcion == 5 or opcion == 11:
    ## Ejercicio 5
    print("Ejercicio 5")
    print(f"""Crear una función llamada segundos_a_horas(segundos) que reciba
    una cantidad de segundos como parámetro y devuelva la cantidad
    de horas correspondientes. Solicitar al usuario los segundos y mos-
    trar el resultado usando esta función.""")

    segundos_correctos = False
    while not segundos_correctos:
        segundos = int(input("Ingresar segundos: "))
        if segundos < 0:
            print("Los segundos no pueden ser negativos. Intente nuevamente.")
        else:
            segundos_correctos = True
    print("Llamando a la función segundos_a_horas()")
    segundos_a_horas(segundos)
    print("Llamada a la función segundos_a_horas() finalizada")
    print("Fin Ejercicio 5\n")
    
if opcion == 6 or opcion == 11:
    ## Ejercicio 6
    print("Ejercicio 6")
    print(f"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un
    número como parámetro y imprima la tabla de multiplicar de ese
    número del 1 al 10. Pedir al usuario el número y llamar a la fun-
    ción.""")
    numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
    print("Llamando a la función tabla_multiplicar()")
    tabla_multiplicar(numero)
    print("Llamada a la función tabla_multiplicar() finalizada")   
    
    print("Fin Ejercicio 6\n")

if opcion == 7 or opcion == 11:
    ## Ejercicio 7
    print("Ejercicio 7")
    print(f"""7. Crear una función llamada operaciones_basicas(a, b) que reciba
    dos números como parámetros y devuelva una tupla con el resulta-
    do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
    sultados de forma clara.""")

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    print("Llamando a la función operaciones_basicas()")
    tupla = operaciones_basicas(num1,num2)
    print("Llamada a la función operaciones_basicas() finalizada")
    print(f"Mi tupla: {tupla}")    
    print("Fin Ejercicio 7\n")

if opcion == 8 or opcion == 11:
    ## Ejercicio 8
    print("Ejercicio 8")
    print(f"""8. Crear una función llamada calcular_imc(peso, altura) que reciba el
    peso en kilogramos y la altura en metros, y devuelva el índice de
    masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
    ción para mostrar el resultado con dos decimales.""")

    peso_correcto = False
    altura_correcta = False
    while not peso_correcto:
        peso = float(input("Ingrese su peso en kilogramos: "))
        if peso <= 0:
            print("El peso no puede ser cero o negativo. Intente nuevamente.")
        else:
            peso_correcto = True
    while not altura_correcta:
        altura = float(input("Ingrese su altura en metros: "))
        if altura <= 0:
            print("La altura no puede ser cero o negativa. Intente nuevamente.")
        else:
            altura_correcta = True

    print("Llamando a la función calcular_imc()")
    calcular_imc(peso, altura)
    print("Llamada a la función calcular_imc() finalizada")
    
    print("Fin Ejercicio 8\n")

if opcion == 9 or opcion == 11:
    ## Ejercicio 9
    print("Ejercicio 9")
    print(f"""9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
    una temperatura en grados Celsius y devuelva su equivalente en
    Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
    resultado usando la función.""")

    celsius_correcto = False
    while not celsius_correcto:
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        if celsius < -273.15:
            print("La temperatura no puede ser menor al cero absoluto (-273.15 °C). Intente nuevamente.")
        else:
            celsius_correcto = True
    print("Llamando a la función celsius_a_fahrenheit()")
    celsius_a_fahrenheit(celsius)
    print("Llamada a la función celsius_a_fahrenheit() finalizada")
    
    print("Fin Ejercicio 9\n")

if opcion == 10 or opcion == 11:
    ## Ejercicio 10
    print("Ejercicio 10")
    print(f"""10.Crear una función llamada calcular_promedio(a, b, c) que reciba
    tres números como parámetros y devuelva el promedio de ellos.
    Solicitar los números al usuario y mostrar el resultado usando esta
    función.""")

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    print("Llamando a la función calcular_promedio()")
    calcular_promedio(num1, num2, num3)
    print("Llamada a la función calcular_promedio() finalizada")

    
    print("Fin Ejercicio 10\n")