import sys
from pathlib import Path
from grafo import Grafo
from algoritmo import Algoritmo

USO = "Uso correcto: python parte-2.py <vertice-1> <vertice-2> <nombre-del-mapa> <salida>"

def main():

    #verifica el nº de argumentos    
    if len(sys.argv) != 5:
        print(USO, file=sys.stderr)
        sys.exit(1)

    #verifica que existe ruta .gr y .co para el nombre del mapa especificado
    ruta_gr = Path(f"{sys.argv[3]}.gr")
    ruta_co = Path(f"{sys.argv[3]}.co")

    #verificar que existe el fichero .gr
    if not ruta_gr.exists(): # si no existe = error
        print(f"Error: no existe el fichero: {ruta_gr}", file=sys.stderr)
        sys.exit(2)

    if not ruta_co.exists(): # si no existe = error
        print(f"Error: no existe el fichero: {ruta_co}", file=sys.stderr)
        sys.exit(2)

    #convertimos los índices a int y establecemos un rango 
    try:
        vertice_1 = int(sys.argv[1])
        vertice_2 = int(sys.argv[2])
    except ValueError:
        print("Error: vértice-1 y vértice-2 deben ser números enteros", fyle=sys.stderr)
        sys.exit(1)

    #guarda la ruta de salida como path
    salida = Path(sys.argv[4])

    grafo = Grafo(ruta_gr, ruta_co)
    algoritmo = Algoritmo(grafo)
    camino, coste, expansiones = algoritmo.dijkstra(vertice_1, vertice_2)



   
