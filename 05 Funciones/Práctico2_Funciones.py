#Práctico 2: Funciones

'''Ejercicio 1: Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!” Llamar a esta función desde el
programa principal.'''

def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

'''Ejercicio 2: Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
volver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.'''

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("¿Cual es tu nombre? ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)

'''Ejercicio 3: Crear una funcion llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parametros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
dir los datos al usuario y llamar a esta funcion con los valores in-
gresados.'''

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("¿Donde vives? ")

informacion_personal(nombre, apellido, edad, residencia)

'''Ejercicio 4: Crear dos funciones: calcular _area_circulo(radio) que reciba el radio como parametro y devuelva el area del circulo. calcular_peri-metro_circulo(radio) que reciba el radio como parametro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.'''

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
radio = float(input("Ingresa el radio del circulo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es: {area:.2f}")
print(f"El perimetro del circulo es: {perimetro:.2f}")

'''Ejercicio 5: Crear una funcion llamada segundos _a_horas(segundos) que reciba una cantidad de segundos como parametro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.'''

def segundos_a_horas(segundos):
    return segundos / 3600
segundos = int(input("Ingresa la cantidad de segundos: "))
horas = segundos_a_horas(segundos)

print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

'''Ejercicio 6: Crear una funcion llamada tabla_multiplicar(numero) que reciba un numero como parametro y imprima la tabla de multiplicar de ese numero del 1 al 10. Pedir al usuario el numero y llamar a la funcion.'''

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
numero = int(input("Ingresa un numero para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

'''Ejercicio 7: Crear una funcion llamada operaciones_basicas(a, b) que reciba dos numeros como parametros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.'''

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinida (division por cero)"
    return (suma, resta, multiplicacion, division)
    
a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))

resultado = operaciones_basicas(a, b)

print("\nResultados de las operaciones:")
print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[1]}")
print(f"Multiplicacion: {resultado[2]}")
print(f"Division: {resultado[3]}")

'''Ejercicio 8: Crear una funcion llamada calcular _imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el indice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.'''

def calcular_imc(peso, altura):
    return peso / (altura ** 2)
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Tu indice de masa corporal (IMC) es: {imc:.2f}")

'''Ejercicio 9: Crear una funcion llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.'''

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)

'''Ejercicio 10: Crear una funcion llamada calcular_promedio(a, b, c) que reciba tres numeros como parametros y devuelva el promedio de ellos.
Solicitar los numeros al usuario y mostrar el resultado usando esta funcion. '''

def calcular_promedio(a, b, c):
    return (a + b + c) / 3
a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))
c = float(input("Ingresa el tercer numero: "))

promedio = calcular_promedio(a, b, c)

print(f"El promedio de los tres numeros es: {promedio:.2f}")