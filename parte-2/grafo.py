class Grafo:
    def __init__(self, ruta_gr, ruta_co):
        #inicializamos los diccionarios
        self.vecinos = {} #guarda todos los vertices vecinos de cada vertice y sus costes. (key : vertice, value :  lista de (vertice_vecino, coste))
        self.coordenadas = {} #guarda las coordenadas de cada vertices
        #leemos los archivos para actualizar estos diccionarios
        self.cargarGr(ruta_gr)
        self.cargarCo(ruta_co)
        #una vez hecho esto, el grafo está listo
    
    #lee el archivo mapa.gr y actualiza el diccionario vecinos
    def cargarGr(self, ruta_gr):
        with ruta_gr.open("r", encoding="utf-8") as fichero:
            for linea in fichero: #lee cada linea del fichero
                linea = linea.strip() #eliminamos espacios en blanco al inicio y al final
                #ignoramos cualquier linea vacía o que no empiece por "a"
                if linea.startswith("a"):
                    arco = linea.split() #arco = ['a', vertice-1, vertice-2, coste]
                    
                    #desglosamos arco para que el codigo sea más legible y los guardamos como int para facilitar funcioes futuras
                    vertice_1 = int(arco[1])
                    vertice_2 = int(arco[2])
                    coste = int(arco[3])

                    #si el vertice todavia no está en el diccionario:
                    if vertice_1 not in self.vecinos: 
                        self.vecinos[vertice_1] = [] #andimos key: vertice-1 con valor: lista vacía, preparamos el "contenedor"
                    self.vecinos[vertice_1].append((vertice_2, coste)) #añadimos (vertice-2, coste) a la lista de valores de vertice-1

                    #tambien debemos asegurarnos de que vertice-2 esté en el diccionario (haya key: vertice-2),
                    #para que exista como clave aaunque vertice-2 no tenga nodos adyacentes. 
                    if vertice_2 not in self.vecinos:
                        self.vecinos[vertice_2] = [] #en caso de que no tenga vecinos, devolverá lista vacía

    #lee el archivo mapa.co y actualiza el diccionario coordenadas
    #seguimos la misma implementación que en leerGr, se comentarán unicamente las diferencias
    def cargarCo(self, ruta_co):
        with ruta_co.open("r", encoding="utf-8") as fichero:
            for linea in fichero:
                linea = linea.strip()
                if linea.startswith("v"):
                    coordenadas = linea.split() #coordenadas = ["v", vertice, longitud, latitud]
                    vertice = int(coordenadas[1])
                    longitud = int(coordenadas[2])
                    latitud = int(coordenadas[3])

                    #cada vertice tiene una sola coordenada, ya no hace falta hacer una lista
                    self.coordenadas[vertice] = (longitud, latitud)

#las siguientes funciones acceden a los diccionarios: vecinos y coordenadas. Devuelven el valor deseado (value) del vértice especificado (key)
    
    #devolmemos la lista de vecinos del vertice
    #si no existe devuelve lista vacia []
    def vecinosVertice(self, vertice):
        return self.vecinos.get(vertice, [])

    #devolvemos las coordenadas del vertice indicado
    def coordenadasVertice(self, vertice):
        return self.coordenadas.get(vertice)
    