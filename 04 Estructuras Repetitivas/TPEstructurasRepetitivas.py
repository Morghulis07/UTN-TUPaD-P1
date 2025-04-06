#Práctico 4 : Estructuras repetitivas

'''Ejercicio 1: Crea un programa que imprima en pantalla todos los numeros enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un numero por linea.'''

for i in range(101):
    print(i)

'''Ejercicio 2: Desarrolla un programa que solicite al usuario un numero entero y determine la cantidad de digitos que contiene.'''

numero = input("Ingrese un número entero: ")

if numero.startswith('-'):
    numero = numero[1:]

cantidad_digitos = len(numero)

print("El numero tiene", cantidad_digitos, "digitos.")

'''Ejercicio 3: DEscribe un programa que sume todos los numeros enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.'''

inicio = int(input("Ingrese el primer numero: "))
fin = int(input("Ingrese el segundo numero: "))
menor = min(inicio, fin)
mayor = max(inicio, fin)
suma = 0
for i in range(menor + 1, mayor):
    suma += i
print("La suma de los numeros entre", menor, "y", mayor, "es:", suma)

'''Ejercicio 4: Elabora un programa que permita al usuario ingresar numeros enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.'''

suma = 0
while True:
    numero = int(input("Ingrese un numero entero (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
print("La suma total es:", suma)

'''Ejercicio 5: Crea un juego en el que el usuario deba adivinar un numero aleatorio entre 0 y 9. Al final, el programa debe mostrar cuantos intentos fueron necesarios para acertar el numero.'''

import random
numero_secreto = random.randint(0, 9)
intentos = 0
print("Adivina el numero secreto entre 0 y 9")
while True:
    intento = int(input("Ingresa tu intento: "))
    intentos += 1
    if intento == numero_secreto:
        print(f"Correcto, Adivinaste el numero en {intentos} intento(s).")
        break
    else:
        print("Incorrecto. Intenta de nuevo.")

'''Ejercicio 6: Desarrolla un programa que imprima en pantalla todos los numeros pares comprendidos entre 0 y 100, en orden decreciente.'''

for numero in range(100, -1, -1):
    if numero % 2 == 0:
        print(numero)

'''Ejercicio 7: Crea un programa que calcule la suma de todos los numeros comprendidos entre 0 y un numero entero positivo indicado por el usuario.'''

n = int(input("Ingrese un numero entero positivo: "))
if n < 0:
    print("Por favor, ingrese un numero positivo.")
else:
    suma = 0
    for i in range(n + 1):
        suma += i
    print("La suma de los numeros de 0 a", n, "es:", suma)

'''Ejercicio 8: Crea un programa que calcule la suma de todos los numeros comprendidos entre 0 y un numero entero positivo indicado por el usuario.'''

CANTIDAD = 100
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(CANTIDAD):
    num = int(input(f"Ingrese el numero {i+1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
print("\n--- Resultados ---")
print("Cantidad de numeros pares: ", pares)
print("Cantidad de numeros impares: ", impares)
print("Cantidad de numeros positivos: ", positivos)
print("Cantidad de numeros negativos: ", negativos)

'''Ejercicio 9: Elabora un programa que permita al usuario ingresar 100 numeros enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 
100 numeros cambiando solo un valor).'''

CANTIDAD = 100
suma_total = 0
for i in range(CANTIDAD):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    suma_total += numero
media = suma_total / CANTIDAD
print("\n--- Resultado ---")
print(f"La media de los {CANTIDAD} numeros ingresados es: {media}")

'''Ejercicio 10: Escribe un programa que invierta el orden de los digitos de un numero ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.'''

numero = input("Ingrese un numero entero: ")
numero_invertido = numero[::-1]
print("Numero invertido:", numero_invertido)