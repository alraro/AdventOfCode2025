import math
from collections import Counter

class Box:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def distance_from_box(self, box):
		return math.sqrt(math.pow(self.x - box.x, 2) + math.pow(self.y - box.y, 2) + math.pow(self.z - box.z, 2))
	
	@classmethod
	def parse_box(cls, line):
		x, y, z = line.split(',')
		return cls(int(x), int(y), int(z))
	
	def __str__(self) -> str:
		return f"({self.x}, {self.y}, {self.z})"
	
	def __repr__(self) -> str:
		return self.__str__()


class CircuitManager:
    def __init__(self, n_elements):
        # Al principio, cada caja es su propio padre (su propio circuito aislado)
        self.parent = list(range(n_elements))

    def find(self, i):
        # Busca recursivamente a qué circuito pertenece 'i'
        # (Con 'path compression' para hacerlo ultra rápido)
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        # Une el circuito de la caja 'i' con el circuito de la caja 'j'
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            # Si son diferentes, conectamos uno al otro
            self.parent[root_i] = root_j
            return True # Se hizo una nueva conexión real
        return False # Ya estaban conectados

# --- 3. Lógica Principal ---
def solve():
    boxes = []
    input_file = "Day8/input" # <--- CAMBIA ESTO A TU ARCHIVO REAL (input.txt)

    # A. Leer archivo
    try:
        with open(input_file, "r") as file:
            for line in file:
                box = Box.parse_box(line)
                if box:
                    boxes.append(box)
    except FileNotFoundError:
        print(f"Error: No se encuentra {input_file}")
        return

    n_boxes = len(boxes)
    print(f"Cajas leídas: {n_boxes}")

    # B. Calcular TODAS las distancias entre pares
    # Guardaremos tuplas: (distancia, índice_caja_1, índice_caja_2)
    edges = []
    print("Calculando distancias...")
    for i in range(n_boxes):
        for j in range(i + 1, n_boxes): # i+1 para no repetir pares ni comparar consigo mismo
            dist = boxes[i].distance_from_box(boxes[j])
            edges.append((dist, i, j))

    # C. Ordenar por distancia (menor a mayor)
    edges.sort(key=lambda x: x[0])

    # D. Tomar las 1000 conexiones más cortas
    # NOTA: El problema dice "connect together the 1000 pairs".
    # Si tienes menos de 1000 pares (como en el ejemplo), tomará todos los posibles.
    limit = 1000
    top_edges = edges[:limit]
    
    print(f"Procesando las {len(top_edges)} conexiones más cortas...")

    # E. Unir circuitos
    manager = CircuitManager(n_boxes)
    for dist, i, j in top_edges:
        manager.union(i, j)

    # F. Calcular tamaños de los circuitos finales
    # Para saber el tamaño, buscamos el "padre raíz" de cada caja
    roots = [manager.find(i) for i in range(n_boxes)]
    circuit_sizes = Counter(roots).values()
    
    # Ordenamos los tamaños de mayor a menor
    sorted_sizes = sorted(circuit_sizes, reverse=True)
    
    print(f"Tamaños de circuitos encontrados: {sorted_sizes}")

    # G. Multiplicar los 3 más grandes
    if len(sorted_sizes) >= 3:
        result = sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2]
        print(f"Top 3 tamaños: {sorted_sizes[0]}, {sorted_sizes[1]}, {sorted_sizes[2]}")
        print(f"RESPUESTA FINAL: {result}")
    else:
        print("No hay suficientes circuitos para calcular el top 3.")

if __name__ == "__main__":
	solve()