from collections import deque

def parse_machine(line):
	parts = line.split(" ")
	lights = list(map(lambda x: True if x == '#' else False, parts[0].strip('[]')))
	temp = 0
	for light in range(len(lights)):
		if lights[light]:
			temp |= (1 << light)
	lights = temp
	buttons = list(map(lambda x: list(map(int, x.strip('()').split(','))), parts[1:-1]))
	button_masks = []
	for button in range(len(buttons)):
		temp = 0
		for num in buttons[button]:
			temp |= (1 << num)
		button_masks.append(temp)
	joltages = list(map(int, parts[-1].strip('{}').split(',')))
	return lights, button_masks, joltages

def get_min_moves(lights, buttons):
	# target_lights: entero (ej: 6 para 0110)
    # buttons: lista de enteros (ej: [10, 5, ...])
    
    start_state = 0  # Todas las luces empiezan apagadas
    queue = deque([(start_state, 0)]) # (estado_actual, pasos)
    visited = {start_state} # Para no repetir estados y entrar en bucles
    
    while queue:
        current_state, presses = queue.popleft()
        
        # ¿Hemos logrado encender las luces correctas?
        if current_state == lights:
            return presses
            
        # Probar a pulsar cada botón
        for button_mask in buttons:
            # La magia del XOR: aplica el botón
            new_state = current_state ^ button_mask
            
            if new_state not in visited:
                visited.add(new_state)
                # Añadimos a la cola con 1 paso más
                queue.append((new_state, presses + 1))
                
    return -1 # Imposible


def main():
	acum = 0
	input_file = "Day10/input"
	with open(input_file, "r") as file:
		lines = list(file.readlines())
	for line in lines:
		lights, buttons, joltages = parse_machine(line.strip())
		acum += get_min_moves(lights, buttons)
		print(f"Lights: {lights}, Buttons: {buttons}, Joltages: {joltages}")
	print(f"Total moves: {acum}")
if __name__ == "__main__":
	main()