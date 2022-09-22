#Ejercicio 1
def lee_grafo_stdin():
	
	vertices = []
	aristas = []

	aux = ""

	cantVert = int(input("Ingrese la Cant. de Vertices: "))
	
	print("Ingrese los Vertices")
	n = 0
	while n<cantVert:
		vertices.append(input())
		n += 1

	print("Ingrese Aristas")
	aux = "0"
	while aux != "":
		aux = input()
		tupla = tuple(aux.split())
		aristas.append(tupla)
	aristas.pop()

	grafo = (vertices,aristas)

	return grafo


#Ejercicio 2
def cuenta_grado(grafo):

	vertices = grafo[0]
	aristas = grafo[1]

	grados = {}

	lista = [vert for arista in aristas for vert in arista]

	for v in vertices:
		grados[v] = lista.count(v)

	return grados


#Ejercicio 3
def lista_a_adyacencia(grafo):

	vertices = grafo[0]
	aristas = grafo[1]

	for columna in vertices:
		columnalist = []
		for fila in vertices:
			aux1 = (columna,fila)
			aux2 = (fila,columna)
			columnalist.append(aristas.count(aux1) + aristas.count(aux2))
		print(columnalist)


#Ejercicio 4
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
			elif arista[1] == vertice: 
				lista.append(arista[0])
		ady.append(lista)

	print(ady)

	c0 = 0
	while c0 < len(ady):
		c1 = c0
		while c1 < len(ady):
			if any(x in ady[c0] for x in ady[c1]):
				ady[c0] += ady[c1]
				ady.remove(ady[c1])
			c1 += 1
		c0 += 1
	
	print(ady)

	compConexa = []
	for compenente in ady:
		compConexa.append(list(set(compenente)))

	return compConexa


#Ejercicio 5
def es_conexo(grafo): 
	compConexa = []
	compConexa = componentes_conexas(grafo) 
	return(len(compConexa) == 1)

print(componentes_conexas((['a', 'b', 'c', 'd', 'e', 'f'], [('a', 'b'), ('b', 'c'), ('c', 'a'), ('d', 'e')])))