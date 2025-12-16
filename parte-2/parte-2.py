import sys, time
from pathlib import Path
from grafo import Grafo
from algoritmo import Algoritmo

USO = "Uso correcto: python parte-2.py <vertice-1> <vertice-2> <nombre-del-mapa> <salida>"


#las siguientes funciones servrian para escribir en el fichero de salida con el formato deseado

def coste_arco(grafo: Grafo, u: int, v: int):
    for w, c in grafo.vecinosVertice(u):
        if w == v:
            return c
    raise ValueError(f"No existe arco {u}->{v}")

def escribir_solucion(ruta_salida: Path, camino: list[int], grafo: Grafo):
    # ejemplo: 1 - (1498) - 308 - (8718) - 309
    piezas = [str(camino[0])]
    for i in range(len(camino) - 1):
        u = camino[i]
        v = camino[i + 1]
        c = coste_arco(grafo, u, v)
        piezas.append(f"- ({c}) - {v}")
    ruta_salida.write_text(" ".join(piezas) + "\n", encoding="utf-8")

#resolvemos las rutas .gr y .co
def resolver_rutas_mapa(nombre_mapa: str) -> tuple[Path, Path]:
    base = Path(nombre_mapa)

    # Si te pasan "algo.gr" o "algo.co", quita esa extensión final
    if str(base).endswith(".gr"):
        base = Path(str(base)[:-3])
    elif str(base).endswith(".co"):
        base = Path(str(base)[:-3])

    # Caso 1: te pasan un directorio (como en tu captura)
    #   USA-road-d.USA/USA-road-d.USA.gr
    if base.exists() and base.is_dir():
        gr = base / (base.name + ".gr")
        co = base / (base.name + ".co")
        return gr, co

    # Caso 2: te pasan el nombre base (USA-road-d.USA)
    # y los ficheros están en el mismo directorio actual
    gr = Path(str(base) + ".gr")
    co = Path(str(base) + ".co")
    return gr, co


def main():

    #verifica el nº de argumentos    
    if len(sys.argv) != 5:
        print(USO, file=sys.stderr)
        sys.exit(1)

    #verifica que existe ruta .gr y .co para el nombre del mapa especificado
    ruta_gr, ruta_co = resolver_rutas_mapa(sys.argv[3])


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
        print("Error: vértice-1 y vértice-2 deben ser números enteros", file=sys.stderr)
        sys.exit(1)

    #guarda la ruta de salida como path
    salida = Path(sys.argv[4])

    grafo = Grafo(ruta_gr, ruta_co)

    # validar que existen como claves 
    if vertice_1 not in grafo.vecinos or vertice_2 not in grafo.vecinos:
        print("Error: alguno de los vértices no existe en el mapa", file=sys.stderr)
        sys.exit(3)

    algoritmo = Algoritmo(grafo)

    t_inicial = time.perf_counter() #medimos tiempo inicial
    camino, coste, expansiones, n_procesados, arcos_procesados = algoritmo.aEstrella_h1(vertice_1, vertice_2)
    t_final = time.perf_counter() #medimos tiempo final

    tiempo = t_final - t_inicial #calculamos el tiempo de ejecucion

    # imrpime por pantalla:
    print(f"# vertices: {n_procesados}") #nº de vertices procesados
    print(f"# arcos : {arcos_procesados}") #nº de arcos procesados

    #si camino esta vacio entonces no se ha encontrado solucion
    if camino is None:
        print("No se ha encontrado solución")
        salida.write_text("No se ha encontrado camino", encoding="utf-8")
        sys.exit(0)

    #si hay solucion, imprime la solucion óptima encontrada
    print(f"Solución óptima encontrada con coste {coste}\n")

    # nodes/sec
    if tiempo > 0:
        nodes_sec = expansiones / tiempo
    else:
        nodes_sec = float("inf")

    #tiempo de ejecucion calculado anteriormente
    print(f"Tiempo de ejecución: {tiempo:.2f} segundos")
    #nº de nodos expandidos (nodos en la lista cerrada)
    print(f"# expansiones : {expansiones} ({nodes_sec:.2f} nodes/sec)")

    #escribe en el fichero de salida con el formato pedido
    escribir_solucion(salida, camino, grafo)

if __name__ == "__main__":
    main()
   
"""
Hay que imprimir por pantalla:
# numero de vertices PROCESADOS
# numero de arcos PROCESADOS
Coste de la solucion óptima encontrada
Tiempo de ejecucion
# numero de nodos EXPANDIDOS

En el fichero de salida: 
<vertice_1> -<coste para ir de vertice_1 al siguiente>- <vertice_i> -...- <vertice_2>
"""