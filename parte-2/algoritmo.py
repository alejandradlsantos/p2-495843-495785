class Algoritmo:
    def __init__ (self, grafo):
        self.grafo = grafo 

    #implementamos el algoritmo A*
    def aEstrella(self, vertice_1, vertice_2, heuristica):
        abierta = self.abierta
        cerrada = []
        exito = False
        while len(abierta) != 0 or exit == False:
            nodo = abierta.pop(0) #quitamos el primer nodo de abierta
            cerrada.append(nodo) #metemos este nodo en la lista de nodos cerrados
            if nodo == vertice_2:
                exito = True
            else:
                nodo = abierta.pop()

        

        return camino, coste, expansiones

    #funcion heurísitca 0, h() = 0. Dijkstra
    def dijkstra(self, vertice_1, vertice_2):
        return self.aEstrella(vertice_1, vertice_2, 0)
    
    #funcion heurísitca 1, distancia euclídea.
    def aEstrella_h1(self, vertice_1, vertice_2):
        return self.aEstrella(vertice_1, vertice_2, self.h1(vertice_1, vertice_2))
    
    #funcion heurísitca 2, distania euclídea con factor k para escalar la distancia euclidea. 
    def aEstrella_h2(self, vertice_1, vertice_2, k):
        return self.aEstrella(vertice_1, vertice_2, self.h2(vertice_1, vertice_2, k))

    #implementamos las fórmulas para las heurísticas h1 y h2
    def h1(self, vertice_1, vertice_2):
        lat_1, lon_1 = vertice_1.lat, vertice_1.lon
        lat_2, lon_2 = vertice_2.lat, vertice_2.lon

        distancia_x = lat_1 - lat_2
        distancia_y = lon_1 - lon_2

        return (distancia_x*distancia_x + distancia_y*distancia_y)
    
    def h2(self, vertice_1, vertice_2, k):
        return k * self.h1(vertice_1, vertice_2)
