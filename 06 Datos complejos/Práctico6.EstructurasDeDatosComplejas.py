#Práctico 6: Estructuras de datos complejas

'''Ejercicio 1: Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300 '''

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melon': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

'''Ejercicio 2: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800 '''

precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450,'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800
print(precios_frutas)

'''Ejericico 3: Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.'''

precios_frutas = {'Banana': 1330, 'Anana': 2500, 'Melon': 2800, 'Uva': 1450,'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}
frutas = list(precios_frutas.keys())
print(frutas)

'''Ejercicio 4: Crear una clase llamada Persona que contenga un método __init__ con los atributos nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un mensaje de salud que siga
 la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad] años."'''

class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad
    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")
persona1 = Persona("Juan", "España", 25)
persona1.saludar()

'''Ejercicio 5: Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente. 
Ayuda: el módulo math puede ser de utilidad para usar la constante 𝜋 . '''

import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        return area
    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro
mi_circulo = Circulo(5)
print("Área:", mi_circulo.calcular_area())
print("Perímetro:", mi_circulo.calcular_perimetro())

'''Ejercicio 6: Dado un string con paréntesis "()" , "{}" , "[]" , verifica si están correctamente balanceados usando una pila.'''

def esta_balanceado(cadena):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}
    for caracter in cadena:
        if caracter in "([{":
            pila.append(caracter)
        elif caracter in ")]}":
            if not pila or pila[-1] != pares[caracter]:
                return False
            pila.pop()
    return len(pila) == 0
print(esta_balanceado("([]){}"))
print(esta_balanceado("([)]"))      
print(esta_balanceado("((()))"))     
print(esta_balanceado("((())"))    

'''Ejercicio 7: Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir:
● Agregar clientes ( encolar ).
● Atender clientes ( desencolar ).
● Mostrar el siguiente cliente en la fila.'''

from collections import deque
class Banco:
    def __init__(self):
        self.cola = deque()
    def encolar_cliente(self, nombre):
        self.cola.append(nombre)
        print(f"Cliente {nombre} agregado a la fila.")
    def atender_cliente(self):
        if self.cola:
            cliente = self.cola.popleft()
            print(f"Atendiendo al cliente: {cliente}")
        else:
            print("No hay clientes en la fila.")
    def siguiente_cliente(self):
        if self.cola:
            print(f"Siguiente cliente en la fila: {self.cola[0]}")
        else:
            print("La fila esta vacia.")
banco = Banco()
banco.encolar_cliente("Ana")
banco.encolar_cliente("Luis")
banco.encolar_cliente("Carla")
banco.siguiente_cliente()   
banco.atender_cliente() 
banco.siguiente_cliente()

'''Ejercicio 8: Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar los valores almacenados. '''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    def insertar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.valor)
            actual = actual.siguiente
lista = ListaEnlazada()
lista.insertar_al_inicio(10)
lista.insertar_al_inicio(20)
lista.insertar_al_inicio(30)
lista.mostrar_lista()

'''Ejercicio 9: Dada una lista enlazada, implementa una función para invertirla.'''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    def insertar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.valor)
            actual = actual.siguiente
    def invertir_lista(self):
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior
lista = ListaEnlazada()
lista.insertar_al_inicio(10)
lista.insertar_al_inicio(20)
lista.insertar_al_inicio(30)
print("Lista original:")
lista.mostrar_lista()
lista.invertir_lista()
print("Lista invertida:")
lista.mostrar_lista()

