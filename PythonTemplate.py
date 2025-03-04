# Importación de módulos
import os
import sys
import math
import random
import datetime
import json
import re

# Variables y tipos de datos
x = 10         # int
y = 3.14       # float
name = "Mathias"  # str
is_active = True  # bool
nums = [1, 2, 3]  # list
data = (4, 5, 6)  # tuple
info = {"name": "Mathias", "age": 23}  # dict
s = {1, 2, 3}  # set

# Operadores básicos
a, b = 10, 3
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b
exponente = a ** b
division_entera = a // b

# Estructuras de control
if a > b:
    print("A es mayor")
elif a == b:
    print("Son iguales")
else:
    print("B es mayor")

for i in range(5):
    print(i)

while a > 0:
    print(a)
    a -= 1

# Funciones
def saludar(nombre):
    return f"Hola, {nombre}"

print(saludar("Mathias"))

# Clases y POO
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Soy {self.nombre} y tengo {self.edad} años."

p1 = Persona("Mathias", 23)
print(p1.presentarse())

#  Manejo de archivos
with open("archivo.txt", "w") as f:
    f.write("Hola Mundo!")

with open("archivo.txt", "r") as f:
    print(f.read())

# Expresiones Regulares
pattern = r"\d+"
match = re.search(pattern, "Edad: 23")
if match:
    print("Número encontrado:", match.group())

# JSON
json_data = json.dumps(info)  # Convertir diccionario a JSON
print(json_data)

info_dict = json.loads(json_data)  # Convertir JSON a diccionario
print(info_dict)

# Fechas y Tiempos
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Generación de números aleatorios
rand_num = random.randint(1, 100)
print(rand_num)

# Manejo de Excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)

# List Comprehensions
cuadrados = [x**2 for x in range(10)]
print(cuadrados)

# Funciones Lambda
doblar = lambda x: x * 2
print(doblar(5))

# Map, Filter, Reduce
from functools import reduce
nums = [1, 2, 3, 4, 5]

doblados = list(map(lambda x: x * 2, nums))
pares = list(filter(lambda x: x % 2 == 0, nums))
suma_total = reduce(lambda x, y: x + y, nums)

print(doblados, pares, suma_total)
