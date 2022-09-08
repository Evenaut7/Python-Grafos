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


#Ejercicio 5
def es_conexo(grafo): 
	compConexa = []
	compConexa = componentes_conexas(grafo) 
	return(len(compConexa) == 1)