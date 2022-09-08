def cuenta_grado(grafo):

	vertices = grafo[0]
	aristas = grafo[1]

	grados = {}

	lista = [vert for arista in aristas for vert in arista]

	for v in vertices:
		grados[v] = lista.count(v)

	return grados

def componentes_conexas(grafo):

	vertices = grafo[0]
	aristas = grafo[1]

	ady = []
	for vertice in vertices:
		lista = []
		lista.append(vertice)
		for arista in aristas:
			if arista[0] == vertice: 
				lista.append(arista[1])
			else:
				if arista[1] == vertice: 
					lista.append(arista[0])
		ady.append(lista)

	c0 = 0
	while c0 < len(ady):
		for comp in ady:
			if any(x in ady[c0] for x in comp):
				ady[c0] = ady[c0] + comp
		c0 += 1

	c1 = 0
	while c1 < len(ady):
		for compe in ady:
			if(ady[c1] != compe):
				if any(x in ady[c1] for x in compe):
					ady.remove(compe)
		c1 += 1

	compConexa = []

	for compenente in ady:
		compConexa.append(list(set(compenente)))
	
	return(compConexa)

def es_conexo(grafo): 
	compConexa = []
	compConexa = componentes_conexas(grafo) 
	return(len(compConexa) == 1)

#---------------------------------------------------------------------------

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