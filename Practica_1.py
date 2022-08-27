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
	while aux != "-1":
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
def componentes_conexas():
	as




grafo = (['A', 'B', 'C'], [('A', 'A'), ('B', 'A'), ('C', 'B'), ('B', 'A')])

