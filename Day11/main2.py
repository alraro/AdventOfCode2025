from collections import defaultdict
import sys

# Aumentamos el límite de recursión por si el grafo es muy profundo
sys.setrecursionlimit(20000)

class Graph:
    def __init__(self):
        self.graph = defaultdict(set)
        # Diccionario para memorizar resultados y no recalcular
        self.memo = {}

    def add_edge(self, u, v):
        self.graph[u].add(v)

    def count_paths(self, start, end):
        """
        Calcula el número de caminos desde 'start' hasta 'end'
        usando memoización.
        """
        # Limpiamos la memoria antes de empezar una nueva búsqueda principal
        self.memo = {} 
        return self._dfs_count(start, end)

    def _dfs_count(self, current, target):
        # Si llegamos al destino, hemos encontrado 1 camino válido
        if current == target:
            return 1
        
        # Si ya hemos calculado este nodo antes, devolvemos el valor guardado
        if (current, target) in self.memo:
            return self.memo[(current, target)]
        
        total_paths = 0
        # Exploramos vecinos
        if current in self.graph:
            for neighbor in self.graph[current]:
                total_paths += self._dfs_count(neighbor, target)

        # Guardamos el resultado en memoria antes de devolverlo
        self.memo[(current, target)] = total_paths
        return total_paths

    def __str__(self):
        result = ""
        for node, neighbors in self.graph.items():
            result += f"{node}: {', '.join(neighbors)}\n"
        return result

def main():
    input_file = "Day11/input" # Asegúrate de que la ruta es correcta
    try:
        with open(input_file, "r") as file:
            lines = list(file.readlines())
    except FileNotFoundError:
        print(f"Error: No se encuentra el archivo {input_file}")
        return

    graph = Graph()
    for line in lines:
        line = line.strip()
        if not line: continue
        parts = line.split(":")
        node = parts[0].strip()
        # Manejo de nodos que no tienen conexiones o strings vacíos
        if len(parts) > 1 and parts[1].strip():
            connections = parts[1].strip().split(" ")
            for conn in connections:
                graph.add_edge(node, conn)

    # --- LÓGICA PARTE 2 ---
    
    # CASO 1: Orden svr -> dac -> fft -> out
    # Calculamos los tramos individuales
    svr_to_dac = graph.count_paths("svr", "dac")
    dac_to_fft = graph.count_paths("dac", "fft")
    fft_to_out = graph.count_paths("fft", "out")
    
    # Multiplicamos las combinaciones
    total_case_1 = svr_to_dac * dac_to_fft * fft_to_out
    
    # CASO 2: Orden svr -> fft -> dac -> out
    svr_to_fft = graph.count_paths("svr", "fft")
    fft_to_dac = graph.count_paths("fft", "dac")
    dac_to_out = graph.count_paths("dac", "out")
    
    total_case_2 = svr_to_fft * fft_to_dac * dac_to_out
    
    # Suma total
    total_paths = total_case_1 + total_case_2
    
    print(f"--- Desglose ---")
    print(f"Ruta (svr->dac->fft->out): {svr_to_dac} * {dac_to_fft} * {fft_to_out} = {total_case_1}")
    print(f"Ruta (svr->fft->dac->out): {svr_to_fft} * {fft_to_dac} * {dac_to_out} = {total_case_2}")
    print(f"--- Resultado Final ---")
    print(f"Total paths visiting both 'dac' and 'fft': {total_paths}")

if __name__ == "__main__":
    main()