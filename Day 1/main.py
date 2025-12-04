def get_num_vueltas(current, steps, direction):
	if direction == 'L':
		# Yendo a la izquierda desde current, cuántas veces pasamos por 0
		if current == 0:
			# Si empezamos en 0, no lo contamos como el primer paso
			# Pasaremos por 0 cada 100 pasos
			return steps // 100
		elif steps < current:
			# No llegamos a 0
			return 0
		else:
			# Pasamos por 0 al menos una vez
			# Primera vez: después de 'current' pasos (llegamos a 0)
			# Luego: cada 100 pasos adicionales
			remaining_after_first_zero = steps - current
			return 1 + remaining_after_first_zero // 100
	elif direction == 'R':
		# Yendo a la derecha desde current, cuántas veces pasamos por 0
		if current == 0:
			# Si empezamos en 0, no lo contamos como el primer paso
			# Pasaremos por 0 cada 100 pasos
			return steps // 100
		else:
			steps_to_zero = 100 - current
			if steps < steps_to_zero:
				# No llegamos a 0
				return 0
			else:
				# Pasamos por 0 al menos una vez
				remaining_after_first_zero = steps - steps_to_zero
				return 1 + remaining_after_first_zero // 100
    

def main():
	input_file = "input"
	current = 50
	times_0 = 0
	with open(input_file, "r") as file:
		data = file.read()
	for line in data.splitlines():
		direction = line[0]
		steps = int(line[1:])
		vueltas = get_num_vueltas(current, steps, direction)
		print(f"Current before {line}: {current}, times_0: {times_0}")
		times_0 += vueltas
		if direction == 'L':
			current = (current - steps) % 100
		elif direction == 'R':
			current = (current + steps) % 100
		print(f"After {line}: {current}, times_0: {times_0}\n")
	print(f"Password is {times_0}")

main()