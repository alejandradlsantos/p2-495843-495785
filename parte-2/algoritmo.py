from grafo import Grafo
from abierta import Abierta
from cerrada import Cerrada

class Algoritmo:
    def __init__ (self, grafo):
        self.grafo = grafo 

    #implementamos el algoritmo A*
    def aEstrella(self, vertice_1, vertice_2, heuristica):
        #inicializamos la lista abierta (vertices a procesar)y cerrada (vertices expandidos)
        lista_abierta = Abierta() #lista de nodos pendientes
        lista_cerrada = Cerrada() #lista de nodos expandidos
        
        #A* se basa en: funcion de evaluacion (f) = funcion de coste (g) + funcion heurísitca (h)
        lista_costes = {vertice_1: 0} #diccionario que guarda la funcion de coste de cada vertice
        padre = {vertice_1: None} #puntero al nodo anterior en el mejor camino conocido

        #metemos el nodo inicial en la lista abierta 
        evaluacion_inicial = 0 + heuristica(vertice_1, vertice_2)
        lista_abierta.agregarVertice(vertice_1, evaluacion_inicial)

        #variables para contar el número de nodos y arcos procesados
        n_procesados = 1 #inicializamos a 1 porque ya tiene en la lsita vertice-1
        arcos_procesados = 0 #en el vertice uno, todavía no se han mirado vecinos
        
        while not lista_abierta.estaVacia():
            #sacamos vertice con mejor funcion de evaluacion
            vertice = lista_abierta.sacarMejor()

            #si ya lo expandimos, salta
            if lista_cerrada.contiene(vertice):
                continue

            #sino, guarda en la lista de expandidos
            lista_cerrada.agregarVertice(vertice)

            #en cuanto llegamos a vertice_2 (vertice de destino) --> éxito, salimos del bucle y dejamos de buscar
            if vertice == vertice_2:
                break 

            #sino, generamos sucesores del vertice actual
            for vecino, coste_arco in self.grafo.vecinosVertice(vertice):
                arcos_procesados += 1 #cada vecino que miramos es un arco procesado
                #si ya esta en la lista cerrada, no se reexpande
                if lista_cerrada.contiene(vecino):
                    continue
                
                #calculamos nueva funcion de coste para llegar a vecino pasando por ese vertice
                nueva_func_coste = lista_costes[vertice] + coste_arco

                #si es la primera vez que vemos vecino o encontramos un camino mejor:
                if vecino not in lista_costes or nueva_func_coste < lista_costes[vecino]:
                    lista_costes[vecino] = nueva_func_coste
                    padre[vecino] = vertice

                    #calculamos la funcion de evaluacion otra vez
                    evaluacion_vecino = nueva_func_coste + heuristica(vecino, vertice_2)
                    lista_abierta.agregarVertice(vecino, evaluacion_vecino)
                    n_procesados += 1 #sumamos contador de vertices insertados pendientes

        expansiones = lista_cerrada.contarVerticesExpandidos()
        
        #si el bucle termina y el vertice_2 no es´ta en la lista de costes, no se ha encontrado camino
        if vertice_2 not in lista_costes:
            return None, None, expansiones
         
        #reconstruimos el camino desde el objetivo hacia atrás con padre[]
        camino = []
        actual = vertice_2
        while actual is not None:
            camino.append(actual)
            actual = padre[actual]
        camino.reverse()

        return camino, lista_costes[vertice_2], expansiones, n_procesados, arcos_procesados


    #funcion heurísitca 0, dijkstra
    #en h0 probamos la resolución del algoritmo por fuerza bruta, heuristica "base" para ver mejoras en las demas
    def dijkstra(self, vertice_1, vertice_2):
        return self.aEstrella(vertice_1, vertice_2, self.h0)
    
    #funcion heurísitca 1, distancia euclídea.
    def aEstrella_h1(self, vertice_1, vertice_2):
        return self.aEstrella(vertice_1, vertice_2, self.h1)
    
    """ 
    #funcion heurísitca 2, distania euclídea con factor k para escalar la distancia euclidea. 
    def aEstrella_h2(self, vertice_1, vertice_2, k):
        return self.aEstrella(vertice_1, vertice_2, self.h2(vertice_1, vertice_2, k))
 """
#implementamos las fórmulas para las heurísticas h0, h1 y h2
    
    #dijkstra establece la funcon heurística = 0. 
    def h0(self, vertice_1, vertice_2):
        return 0 
    
    #calculamos la distancia euclidea
    def h1(self, vertice_1, vertice_2):
        lon_1, lat_1 = self.grafo.coordenadasVertice(vertice_1)
        lon_2, lat_2 = self.grafo.coordenadasVertice(vertice_2)

        distancia_x = lon_1 - lon_2
        distancia_y = lat_1 - lat_2

        return (distancia_x*distancia_x + distancia_y*distancia_y)
    
    #multiplicamos la distancia euclidea por un factor k
    def h2(self, vertice_1, vertice_2, k):
        return k * self.h1(vertice_1, vertice_2)
