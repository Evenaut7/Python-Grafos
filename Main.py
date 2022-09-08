from Practica_1 import *
from Practica_2 import *

#Presentacion

print("PRACTICA 1")

print("\nEjercicio 1:")
grafo = lee_grafo_stdin()
print(grafo)

print("\nEjercicio 2: Los grados de sus vertices es: ")
print(cuenta_grado(grafo))

print("\nEjercicio 3: su matriz de adyacencia es: ")
lista_a_adyacencia(grafo)

print("\nEjercico 4: sus componentes conexas son: ")
print(componentes_conexas(grafo))

print("\nEjercicio 5: Es conexo?: ")
if es_conexo(grafo): print("Si") 
else: print("No")