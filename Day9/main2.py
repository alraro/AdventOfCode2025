class Tile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, value):
		return isinstance(value, Tile) and self.id == value.id

	def __hash__(self):
		return hash(self.id)

	def get_area(self, other):
		return (abs(self.x - other.x) + 1) * (abs(self.y - other.y) + 1)


def correct(tiles, a, b):
	1

def main():
	tiles = []
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
		tiles.append(Tile(x, y))
	i = 0
	while i < len(tiles) - 1:
		curr = tiles[i]
		area = curr.get_area(other)
		biggest = max(biggest, area)
	print("Biggest area:", biggest)
if __name__ == "__main__":
	main()