import math

# --- CLASE BOX (Igual que antes) ---
class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance_from_box(self, box):
        return math.sqrt((self.x - box.x)**2 + (self.y - box.y)**2 + (self.z - box.z)**2)
    
    @classmethod
    def parse_box(cls, line):
        clean_line = line.strip()
        if not clean_line:
            return None
        x, y, z = clean_line.split(',')
        return cls(int(x), int(y), int(z))
    
    def __repr__(self):
        return f"Box({self.x},{self.y},{self.z})"

# --- CLASE UNION-FIND MEJORADA ---
class CircuitManager:
    def __init__(self, n_elements):
        self.parent = list(range(n_elements))
        # Novedad: Llevamos la cuenta de cuántos grupos aislados quedan
        self.num_groups = n_elements 

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            # Conectamos los dos grupos
            self.parent[root_i] = root_j
            # Al unir dos grupos, el número total de grupos baja en 1
            self.num_groups -= 1
            return True # Indica que la unión fue exitosa (eran grupos distintos)
        return False # Ya estaban conectados

def solve():
    boxes = []
    input_file = "Day8/input" # <--- ¡RECUERDA USAR TU INPUT REAL!

    # 1. Leer archivo
    try:
        with open(input_file, "r") as file:
            for line in file:
                box = Box.parse_box(line)
                if box:
                    boxes.append(box)
    except FileNotFoundError:
        print(f"Error: No se encuentra {input_file}")
        return

    n = len(boxes)
    print(f"Total cajas: {n}")

    # 2. Calcular TODAS las distancias
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = boxes[i].distance_from_box(boxes[j])
            edges.append((dist, i, j))

    # 3. Ordenar por distancia (de menor a mayor)
    edges.sort(key=lambda x: x[0])

    # 4. Procesar conexiones (Algoritmo de Kruskal)
    manager = CircuitManager(n)
    
    print("Conectando circuitos...")
    
    last_connection = None

    for dist, i, j in edges:
        # Intentamos unir las cajas i y j
        connected_now = manager.union(i, j)
        
        if connected_now:
            # Si acabamos de hacer una unión, verificamos si ya terminamos
            if manager.num_groups == 1:
                # ¡BINGO! Solo queda 1 grupo gigante.
                # Esta fue la última conexión necesaria.
                last_connection = (i, j)
                break 

    # 5. Calcular resultado final
    if last_connection:
        idx1, idx2 = last_connection
        box1 = boxes[idx1]
        box2 = boxes[idx2]
        
        result = box1.x * box2.x
        
        print(f"\n--- RESULTADO ENCONTRADO ---")
        print(f"Última conexión entre:")
        print(f"  {box1}")
        print(f"  {box2}")
        print(f"Coordenadas X: {box1.x} y {box2.x}")
        print(f"Multiplicación (Respuesta): {result}")
    else:
        print("Error: Se procesaron todas las aristas y no se unificó el circuito (¿grafo disconexo?)")

if __name__ == "__main__":
    solve()