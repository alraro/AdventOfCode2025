import sys
import copy

class Shape:
    def __init__(self, lines):
        # El ID se extrae de la primera línea "0:"
        self.id = int(lines[0].strip(":\n"))
        self.shape = []
        # Parseamos el grid del shape
        for i, line in enumerate(lines[1:]):
            self.shape.append([])
            for char in line.strip():
                if char == "#":
                    self.shape[i].append(True)
                else:
                    self.shape[i].append(False)
     
    def __str__(self):
        return f"Shape {self.id}:\n" + "\n".join("".join("#" if cell else "." for cell in row) for row in self.shape)
  
    def __repr__(self):
        return self.__str__()

class Region:
    def __init__(self, line):
        parts = line.strip().split()
        dimensions = parts[0].strip(":").split("x")
        self.width = int(dimensions[0])
        self.length = int(dimensions[1])
        # Lista de cantidades requeridas por ID de shape
        self.quantities = list(map(int, parts[1:]))
  
    def __str__(self):
        return f"Region {self.width}x{self.length} with quantities: {self.quantities}"

    def __repr__(self):
        return self.__str__()

# --- Funciones de Transformación (Geometría) ---

def rotate_grid(grid):
    """Rota una matriz 2D 90 grados en sentido horario."""
    return [list(row) for row in zip(*grid[::-1])]

def flip_grid(grid):
    """Voltea una matriz 2D horizontalmente."""
    return [row[::-1] for row in grid]

def get_unique_orientations(base_shape):
    """Genera las 8 variantes (rotaciones y flips) y devuelve las únicas."""
    orientations = []
    current = base_shape
    
    # Probamos 4 rotaciones para el estado normal y 4 para el estado volteado
    for _ in range(2): 
        for _ in range(4):
            # Convertimos a tupla para poder usar set() y filtrar duplicados
            shape_tuple = tuple(tuple(row) for row in current)
            orientations.append(shape_tuple)
            current = rotate_grid(current)
        current = flip_grid(current)
    
    # Eliminamos duplicados (ej. un cuadrado es igual rotado) y convertimos de nuevo a listas
    unique_set = set(orientations)
    return [list(list(cell for cell in row) for row in shape) for shape in unique_set]

# --- Lógica de Colocación ---

def can_place_shape(space, shape_grid, r, c):
    """Verifica si el shape cabe en la posición (r, c) sin salirse ni chocar."""
    shape_h = len(shape_grid)
    shape_w = len(shape_grid[0])
    space_h = len(space)
    space_w = len(space[0])

    # 1. Verificar límites del tablero
    if r + shape_h > space_h or c + shape_w > space_w:
        return False

    # 2. Verificar colisiones
    for i in range(shape_h):
        for j in range(shape_w):
            if shape_grid[i][j]:  # Si la pieza tiene bloque aquí
                if space[r + i][c + j]:  # Y el espacio ya está ocupado
                    return False
    return True

def place_shape(space, shape_grid, r, c, value):
    """
    Coloca (value=True) o quita (value=False) una pieza del tablero.
    Modifica 'space' in-place.
    """
    shape_h = len(shape_grid)
    shape_w = len(shape_grid[0])
    
    for i in range(shape_h):
        for j in range(shape_w):
            if shape_grid[i][j]:
                space[r + i][c + j] = value

# --- Algoritmo Principal (Backtracking) ---

def try_fill(space, quantities, shapes):
    # Caso base: Si no quedan cantidades de ningún shape por colocar, hemos tenido éxito.
    if all(qty == 0 for qty in quantities):
        return True

    # Buscamos el primer shape que necesitamos colocar (optimización simple: orden por índice)
    try:
        # Encontramos el índice del primer shape con cantidad > 0
        shape_idx = next(i for i, qty in enumerate(quantities) if qty > 0)
    except StopIteration:
        return True

    original_shape_grid = shapes[shape_idx].shape
    
    # Generamos todas las variantes posibles (rotaciones/flips) de esta pieza
    variants = get_unique_orientations(original_shape_grid)
    
    space_h = len(space)
    space_w = len(space[0])

    # Intentamos colocar la pieza en cada celda del tablero
    for r in range(space_h):
        for c in range(space_w):
            # Y para cada celda, probamos todas las orientaciones posibles
            for variant in variants:
                if can_place_shape(space, variant, r, c):
                    # 1. Colocar pieza
                    place_shape(space, variant, r, c, True)
                    quantities[shape_idx] -= 1
                    
                    # 2. Recursión: intentar colocar las siguientes
                    if try_fill(space, quantities, shapes):
                        return True # Éxito en cascada
                    
                    # 3. Backtracking: Si falló, deshacer cambios
                    quantities[shape_idx] += 1
                    place_shape(space, variant, r, c, False)
    
    return False

def can_fill_region(region, shapes):
    # Crear un grid vacío (False = vacío, True = ocupado)
    space = [[False for _ in range(region.width)] for _ in range(region.length)]
    
    # Hacemos una copia de quantities para no modificar el objeto original permanentemente
    quantities_copy = region.quantities[:]
    
    # Comprobación rápida de área: si el área total de los regalos > área de la región, fallar rápido.
    total_region_area = region.width * region.length
    total_presents_area = 0
    for idx, qty in enumerate(quantities_copy):
        shape_area = sum(sum(1 for cell in row if cell) for row in shapes[idx].shape)
        total_presents_area += shape_area * qty
        
    if total_presents_area > total_region_area:
        return False

    return try_fill(space, quantities_copy, shapes)

def parse_input(lines):
    present_num = 6
    shapes = []
    regions = []
 
    # Parsear los shapes (los bloques separados por saltos de línea al inicio)
    # Nota: Tu lógica asumía un número fijo o estructura fija, aquí la adaptamos ligeramente
    while lines and present_num > 0:
        try:
            end = lines.index("\n") # Buscar línea vacía
        except ValueError:
            # Si no hay más líneas vacías, puede ser el final del bloque de shapes
            # pero necesitamos distinguir si estamos leyendo regiones o el último shape.
            # Asumiremos que si la linea empieza por digito y tiene ":", es shape.
            # Si empieza por "NxM", es region.
            pass
            
        # Un hack seguro para el formato del problema es detectar si la linea parece una region
        if lines[0][0].isdigit() and 'x' in lines[0]:
             break # Dejamos de parsear shapes, empezamos con regiones
             
        if "\n" in lines:
            end = lines.index("\n")
            shape_lines = lines[:end]
            shapes.append(Shape(shape_lines))
            lines = lines[end+1:]
        else:
            # Caso borde si no hay newline al final del último shape antes de regiones
            # (Aunque el formato AoC suele tener newlines)
            # Para simplificar, asumimos que el formato es estricto con separadores.
            break
            
        present_num -= 1
    
    # Parsear regiones
    for line in lines:
        if line.strip():
            regions.append(Region(line))
   
    return shapes, regions

def main():
    # Asegúrate de que este archivo existe con el input copiado
    input_file = "Day12/test" 
    acum = 0
    
    try:
        with open(input_file, "r") as file:
            lines = list(file.readlines())
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{input_file}'.")
        print("Crea un archivo llamado 'input' y pega el input del problema.")
        return

    shapes, regions = parse_input(lines)

    print(f"Procesando {len(regions)} regiones...")
    for i, region in enumerate(regions):
        # Feedback visual simple
        print(f"Checking region {i+1}/{len(regions)} ({region.width}x{region.length})... ", end="")
        if can_fill_region(region, shapes):
            print("Fits!")
            acum += 1
        else:
            print("No fit.")
   
    print(f"Total regions that can be filled: {acum}")

if __name__ == "__main__":
    main()