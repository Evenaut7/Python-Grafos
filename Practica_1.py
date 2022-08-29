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
	i = 0
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

	caminos = []
	for comp in ady:
		for	check in ady:
			if any(x in comp for x in check):
				caminos.append(comp + check)

	compConexas = []

	for x in caminos:
		compConexas.append(list(dict.fromkeys(x)))

	print(compConexas)

	aux = 0
	while aux < len(compConexas):
		aux0 = 0
		while aux0 < len(compConexas):
			if(all(x in compConexas[aux] for x in compConexas[aux0])):
				compConexas.remove(compConexas[aux0])

	print(compConexas)		
				


grafo = (['A', 'B', 'C', 'D'], [('A', 'A'), ('B', 'A'), ('C', 'B'), ('B', 'A')])

componentes_conexas(grafo)