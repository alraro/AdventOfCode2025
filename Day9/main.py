def get_area(a, b):
	return (abs(a[0] - b[0]) + 1) * ((abs(a[1] - b[1])) + 1)

def main():
	tiles = set()
	biggest = 0
	input_file = "Day9/input"
	# input_file = "Day 2/test"
	with open(input_file, "r") as file:
		lines = list(file.readlines())
	for line in lines:
		line = line.strip()
		x, y = line.split(",")
		x = int(x)
		y = int(y)
		tiles.add((x, y))
	while len(tiles) > 1:
		curr = tiles.pop()
		for other in tiles:
			area = get_area(curr, other)
			biggest = max(biggest, area)
	print("Biggest area:", biggest)
if __name__ == "__main__":
	main()