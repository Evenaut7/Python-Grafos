from Practica_1 import *

#Ejercicio 1
def grados_pares(grafo):
    
    grados_pares = True 

    grados = cuenta_grado(grafo)

    for v in grados:
        grados_pares = grados_pares and ((grados[v] % 2) == 0)

    return grados_pares


def graph_has_eulerian_circuit(grafo):

   return grados_pares(grafo) and es_conexo(grafo)


#Ejercicio 2




grafo = (['A', 'B', 'C'], [('A', 'B'), ('B', 'C'), ('C', 'A')])

print (graph_has_eulerian_circuit(grafo))