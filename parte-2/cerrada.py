#contiene todos los nodos que ya han sido expandidos
class Cerrada:
    def __init__(self):
        #inicializamos un set vacío para que luego quea más facil y rápido buscar
        self.vertices_expandidos = set() #además con set controlamos duplicados

    def agregarVertice(self, vertice):
        self.vertices_expandidos.add(vertice)
    
    def contiene(self, vertice):
        return vertice in self.vertices_expandidos

    def contarVerticesExpandidos(self):
        return len(self.vertices_expandidos)
