from this import d
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
def find_eulerian_circuit(grafo):
    
    if graph_has_eulerian_circuit(grafo):
        vertices = grafo[0]

        vertice = vertices[0]
        circuito = [vertice[0]]


        while grafo[1] != []:
            for arista in grafo[1]:
                grados = cuenta_grado(grafo)
                if arista[0] == vertice:
                    grafo[1].remove(arista)
                    if es_conexo(grafo):
                        vertice = arista[1]
                        circuito.append(vertice)
                    else:
                        if grados[vertice] == 1:
                            vertice = arista[1]
                            circuito.append(vertice)
                        else:
                            grafo[1].append(arista)
                elif arista[1] == vertice:
                    grafo[1].remove(arista)
                    if es_conexo(grafo):
                        vertice = arista[0]
                        circuito.append(vertice)
                    else:
                        if grados[vertice] == 1:
                            vertice = arista[0]
                            circuito.append(vertice)
                        else:
                            grafo[1].append(arista)

        return circuito

grafo = (['A', 'B', 'C'], [('A', 'B'), ('B', 'C'), ('C', 'A')])

grafo2 = (['A', 'B' ,'C' ,'D', 'E'], [('A', 'B'),('A', 'C'),('A', 'D'),('A', 'E'),('B', 'C'),('B', 'D'),('B', 'E'),('C', 'D'),('C', 'E'),('D', 'E')])

print (graph_has_eulerian_circuit(grafo2))

print (find_eulerian_circuit(grafo2))