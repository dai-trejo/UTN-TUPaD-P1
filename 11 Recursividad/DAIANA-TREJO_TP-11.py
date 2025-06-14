##########

print("Trabajo Práctico 7")
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
print("9) Todos")
print("10) Salir")

opcion = int(input("Ingrese su opción: "))

if opcion == 1 or opcion == 9:
    print("Ejercicio 1")
    print(f"""Crea una función recursiva que calcule el factorial de un número.
          Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros
          entre 1 y el número que indique el usuario""")


    def factorial(n): 
        return 1 if n == 0  else n * factorial(n - 1)
    num = int(input("Ingrese un número: "))
    
    for i in range(1, num + 1):
        print(f"El factorial de {i} es: {factorial(i)}")     
    print("Fin Ejercicio 1\n")

if opcion == 2 or opcion == 9:
    print("Ejercicio 2")
    print(f"""Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
          indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
          especifique.""")
    
    def fibo(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibo(n - 1) + fibo(n - 2)
        
    num = int(input("Ingrese un número: "))
    print(f"La serie de Fibonacci hasta la posición {num} es: ", end="")
    for i in range(num + 1):
        print(fibo(i), end=" ")
    print()
    print(f"\nEl valor de la serie de Fibonacci en la posición {num} es: {fibo(num)}")


    print("Fin Ejercicio 2\n")

if opcion == 3 or opcion == 9:
    print("Ejercicio 3")
    print(f"""Crea una función recursiva que calcule la potencia de un número base elevado a un
    exponente, utilizando la fórmula n^m = n ∗ n^(m−1). Prueba esta función en un algoritmo general.""")

    def expRecursivo(base,exponente):
        return 1 if exponente == 0 else base * expRecursivo(base, exponente - 1)

    base = int(input("Ingrese la base: "))
    exp = int(input("Ingrese el exponente: "))
    resultado = expRecursivo(base,exp)
    print(resultado)

    print("Fin Ejercicio 3\n")
if opcion == 4 or opcion == 9:
    print("Ejercicio 4")
    print(f"""Crear una función recursiva en Python que reciba un número entero positivo en base
          decimal y devuelva su representación en binario como una cadena de texto.""")
    def binario(num):
       return str(num) if num < 2 else binario(num//2) + str(num%2)
    numero = int(input("Ingrese un numero entero: "))
    print(f"El numero {numero} en binario es: {binario(numero)}")
        
    print("Fin Ejercicio 4\n")

if opcion == 5 or opcion == 9:
    print("Ejercicio 5")
    print(f"""Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
          cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
          lo es.
          Requisitos:
          La solución debe ser recursiva.
          No se debe usar [::-1] ni la función reversed().""")
    def es_palindromo(palabra):
        palabra = palabra.lower()
        longitud = len(palabra)        
        if longitud <= 1:
            return True
        if palabra[0] == palabra[longitud-1]:
            return es_palindromo(palabra[1:longitud-1])
        return False
    palabra_test = input("Ingrese una palabra: ")
    if es_palindromo(palabra_test):
        print(f"{palabra_test} es palindromo")
    else:
        print(f"{palabra_test} NO es palindromo")
    print("Fin Ejercicio 5\n")
if opcion == 6 or opcion == 9:
    print("Ejercicio 6")
    print(f"""Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
          número entero positivo y devuelva la suma de todos sus dígitos.
          Restricciones:
          No se puede convertir el número a string.
          Usá operaciones matemáticas (%, //) y recursión.
          
          Ejemplos:
          suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
          suma_digitos(9) → 9
          suma_digitos(305) → 8 (3 + 0 + 5)""")
    
    def suma_digitos(n):
        if n == 0:
            return 0
        else:
            return n % 10 + suma_digitos(n // 10)
    num = int(input("Ingrese un número entero positivo: "))
    resultado = suma_digitos(num)
    print(f"La suma de los dígitos de {num} es: {resultado}")

    print("Fin Ejercicio 6\n")
if opcion == 7 or opcion == 9:
    print("Ejercicio 7")
    print(f"""Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques,
          en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
          último nivel con un solo bloque.
          Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
          nivel más bajo y devuelva el total de bloques que necesita para construir toda la
          pirámide.
          Ejemplos:
          contar_bloques(1) → 1 (1)
          contar_bloques(2) → 3 (2 + 1)
          contar_bloques(4) → 10 (4 + 3 + 2 + 1)""")
    def contar_bloques(base):
        return 1 if base == 1 else base + contar_bloques(base-1)
    
    base = int(input("Ingrese la base de la primamide: "))
    print(f"La base de la primamide tiene: {base} bloques, por lo que tiene un total de {contar_bloques(base)} bloques")
    
    print("Fin Ejercicio 7\n")
if opcion == 8 or opcion == 9:
    ## Ejercicio 8
    print("Ejercicio 8")
    print(f"""Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
          número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
          aparece ese dígito dentro del número.
          Ejemplos:
          contar_digito(12233421, 2) → 3
          contar_digito(5555, 5) → 4
          contar_digito(123456, 7) → 0""")
    def contar_digito(numero, digito):
        if numero == 0:
            return 0
        else:
            return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)
    numero = int(input("Ingrese un número entero positivo: "))
    digito = int(input("Ingrese un dígito (entre 0 y 9): "))
    if 0 <= digito <= 9:
        resultado = contar_digito(numero, digito)
        print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")
    else:
        print("El dígito debe estar entre 0 y 9.")


    print("Fin Ejercicio 8\n")