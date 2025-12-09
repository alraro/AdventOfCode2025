class Tile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, value):
		return isinstance(value, Tile) and self.x == value.x and self.y == value.y

	def __hash__(self):
		return hash((self.x, self.y))

	def get_area(self, other):
		return (abs(self.x - other.x) + 1) * (abs(self.y - other.y) + 1)


class Board:
	x_min = int(1e9)
	x_max = int(-1e9)
	y_min = int(1e9)
	y_max = int(-1e9)
	tiles = []
	count = 0

	def __init__(self):
		pass
  
	def add_tile(self, tile):
		self.tiles.append(tile)
		self.count += 1
		self.x_max = max(self.x_max, tile.x)
		self.x_min = min(self.x_min, tile.x)
		self.y_max = max(self.y_max, tile.y)
		self.y_min = min(self.y_min, tile.y)

	def get_tile(self, index):
		return self.tiles[index % self.count]

	def __str__(self):
		if (self.x_max - self.x_min) > 100 or (self.y_max - self.y_min) > 100:
			return f"Board too big to print: {self.x_max-self.x_min}x{self.y_max-self.y_min}"

		header = f"Board with {self.count} tiles\nDimensions: x[{self.x_min}, {self.x_max}] y[{self.y_min}, {self.y_max}]\n"
		for i in range(self.y_min - 1, self.y_max + 2):
			for j in range(self.x_min - 2, self.x_max + 3):
				tile = Tile(j, i)
				if tile in self.tiles:
					header += "#"
				else:
					header += "."
			header += "\n"
		return header

	def __repr__(self):
		return str(self)

	def is_inside(self, corner1, corner2):
		for i in range(1, self.count):
			prev = self.get_tile(i - 1)
			curr = self.get_tile(i)
			return True

	def get_biggest_area(self):
		biggest = 0
		i = 0
		while i < self.count - 1:
			curr = self.get_tile(i)
			j = i + 1
			while j < self.count:
				other = self.get_tile(j)
				if not self.is_inside(curr, other):
					j += 1
					continue
				area = curr.get_area(other)
				biggest = max(biggest, area)
				j += 1
			i += 1
		return biggest
 
def main():
	board = Board()
	input_file = "Day9/test"
	with open(input_file, "r") as file:
		lines = list(file.readlines())
	for line in lines:
		line = line.strip()
		x, y = line.split(",")
		board.add_tile(Tile(int(x), int(y)))
	biggest = board.get_biggest_area()
	print(board)
	print("Biggest area:", biggest)
if __name__ == "__main__":
	main()