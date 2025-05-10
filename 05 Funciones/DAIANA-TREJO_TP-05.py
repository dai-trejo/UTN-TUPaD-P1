# -----------------------------------------------------------
# Ejercicio 1
# Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
# -----------------------------------------------------------

# Uso la función range para generar los números del 4 al 100 que sean múltiplos de 4
multiplos_de_4 = list(range(4, 101, 4))

# Imprimo la lista resultante para verificar que esté correcta
print("Lista de múltiplos de 4 del 1 al 100:", multiplos_de_4)




# -----------------------------------------------------------
# Ejercicio 2
# Crear una lista con cinco elementos (colocar los elementos que más te gusten) 
# y mostrar el penúltimo. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona 
# el indexing con números negativos!
# -----------------------------------------------------------

# Creo una lista con cinco cosas 
mis_favoritos = ["campo", "perros", "gatos", "música", "playa"]

# Muestro el penúltimo elemento usando índice negativo (-2)
print("El penúltimo elemento es:", mis_favoritos[-2])




# -----------------------------------------------------------
# Ejercicio 3
# Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
# Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. 
# Por ejemplo: lista_vacia = []
# -----------------------------------------------------------

# Primero creo una lista vacía
lista_vacia = []

# Agrego tres palabras a la lista usando append
lista_vacia.append("computadora")
lista_vacia.append("programación")
lista_vacia.append("python")

# Muestro la lista resultante por pantalla
print("Lista con tres palabras agregadas:", lista_vacia)




# -----------------------------------------------------------
# Ejercicio 4
# Reemplazar el segundo y último valor de la lista “animales” 
# con las palabras “loro” y “oso”, respectivamente.  
# Imprimir la lista resultante por pantalla.
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona 
# el indexing con números negativos!
# -----------------------------------------------------------

# Declaro la lista original de animales
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazo el segundo elemento (índice 1) por "loro"
animales[1] = "loro"

# Reemplazo el último elemento usando índice negativo (-1) por "oso"
animales[-1] = "oso"

# Muestro la lista modificada por pantalla
print("Lista de animales modificada:", animales)




# -----------------------------------------------------------
# Ejercicio 5
# Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# -----------------------------------------------------------

# Declaro una lista con cinco números
numeros = [8, 15, 3, 22, 7]

# La función max(numeros) devuelve el número más grande de la lista, en este caso 22
# Luego, el método remove() elimina ese número (22) de la lista
numeros.remove(max(numeros))

# Imprimo la lista resultante, que ya no contiene el número más alto
print("Lista después de eliminar el número más grande:", numeros)

# En resumen: el programa elimina el número más alto de la lista (22) 
# y luego muestra la lista sin ese valor.





# -----------------------------------------------------------
# Ejercicio 6
# Crear una lista con números del 10 al 30 (incluido), haciendo saltos de 5 en 5 
# y mostrar por pantalla los dos primeros.
# -----------------------------------------------------------

# Uso range para crear una lista del 10 al 30 con saltos de 5 en 5
numeros = list(range(10, 31, 5))

# Muestro la lista completa para verificar que esté bien
print("Lista del 10 al 30 de a 5 en 5:", numeros)

# Ahora muestro los dos primeros elementos con slicing
print("Los dos primeros elementos de la lista son:", numeros[:2])




# -----------------------------------------------------------
# Ejercicio 7
# Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” 
# por dos nuevos valores cualesquiera.
#
# autos = ["sedan", "polo", "suran", "gol"]
# -----------------------------------------------------------

# Defino la lista original con cuatro autos
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazo el valor del índice 1 ("polo") por otro valor
autos[1] = "fiat"

# Reemplazo el valor del índice 2 ("suran") por otro valor
autos[2] = "renault"

# Muestro la lista modificada por pantalla
print("Lista de autos modificada:", autos)




# -----------------------------------------------------------
# Ejercicio 8
# Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente.
# Imprimir la lista resultante por pantalla.
# -----------------------------------------------------------

# Creo una lista vacía llamada "dobles"
dobles = []

# Agrego el doble de 5
dobles.append(5 * 2)

# Agrego el doble de 10
dobles.append(10 * 2)

# Agrego el doble de 15
dobles.append(15 * 2)

# Muestro la lista por pantalla
print("Lista con los valores dobles:", dobles)





# -----------------------------------------------------------
# Ejercicio 9
# Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
#
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla.
# -----------------------------------------------------------

# Defino la lista original con los productos de cada cliente
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agrego "jugo" a la lista del tercer cliente (índice 2)
compras[2].append("jugo")

# b) Reemplazo "fideos" por "tallarines" en la lista del segundo cliente (índice 1)
# "fideos" está en la posición 1 de esa sublista
compras[1][1] = "tallarines"

# c) Elimino "pan" de la lista del primer cliente (índice 0)
compras[0].remove("pan")

# d) Imprimo la lista modificada por pantalla
print("Lista de compras modificada:", compras)





# -----------------------------------------------------------
# Ejercicio 10
# Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#
# ● Posición lista_anidada[0]: 15 
# ● Posición lista_anidada[1]: True 
# ● Posición lista_anidada[2][0]: 25.5 
# ● Posición lista_anidada[2][1]: 57.9 
# ● Posición lista_anidada[2][2]: 30.6 
# ● Posición lista_anidada[3]: False 
#
# Imprimir la lista resultante por pantalla.
# -----------------------------------------------------------

# Creo la lista anidada con la estructura que indica la consigna
lista_anidada = [
    15,              # posición 0
    True,            # posición 1
    [25.5, 57.9, 30.6],  # posición 2 (sublista con 3 elementos)
    False            # posición 3
]

# Muestro la lista anidada por pantalla
print("Lista anidada:", lista_anidada)






