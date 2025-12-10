def parse_machine(line):
	parts = line.split(" ")
	lights = list(map(lambda x: True if x == '#' else False, parts[0].strip('[]')))
	buttons = list(map(int, parts[-1].strip('{}').split(',')))
	joltages = list(map(lambda x: list(map(int, x.strip('()').split(','))), parts[1:-1]))
	return lights, buttons, joltages

def main():
	acum = 0
	input_file = "Day10/test"
	with open(input_file, "r") as file:
		lines = list(file.readlines())
	for line in lines:
		lights, buttons, joltages = parse_machine(line.strip())
		print(f"Lights: {lights}, Buttons: {buttons}, Joltages: {joltages}")
if __name__ == "__main__":
	main()