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

class Edge:
	def __init__(self, start: Tile, end: Tile):
		self.start = start
		self.end = end
  
	def is_in_edge(self, tile: Tile):
		if self.start.x == self.end.x:
			if tile.x != self.start.x:
				return False
			return min(self.start.y, self.end.y) <= tile.y <= max(self.start.y, self.end.y)
		else:
			if tile.y != self.start.y:
				return False
			return min(self.start.x, self.end.x) <= tile.x <= max(self.start.x, self.end.x)

	def is_cutting_edge(self, other):
		if not isinstance(other, Edge):
			return False
		if self.start.x == self.end.x and other.start.y == other.end.y:
			return (min(other.start.x, other.end.x) <= self.start.x <= max(other.start.x, other.end.x) and
					min(self.start.y, self.end.y) <= other.start.y <= max(self.start.y, self.end.y))
		if self.start.y == self.end.y and other.start.x == other.end.x:
			return (min(other.start.y, other.end.y) <= self.start.y <= max(other.start.y, other.end.y) and
					min(self.start.x, self.end.x) <= other.start.x <= max(self.start.x, self.end.x))
		return False

class Board:
	x_min = int(1e9)
	x_max = int(-1e9)
	y_min = int(1e9)
	y_max = int(-1e9)
	tiles = []
	edges = []
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
		if self.count > 1:
			self.edges.append(Edge(self.get_tile(self.count - 2), self.get_tile(self.count - 1)))

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

	def is_contained(self, x, y):
		inside = False
		for k in range(self.count):
			p1 = self.get_tile(k)
			p2 = self.get_tile(k + 1)

			if (p1.y > y) != (p2.y > y):
				intersect_x = (p2.x - p1.x) * (y - p1.y) / (p2.y - p1.y) + p1.x
				if x < intersect_x:
					inside = not inside

		return inside

	def is_inside(self, corner1, corner2):
		x_min = min(corner1.x, corner2.x)
		x_max = max(corner1.x, corner2.x)
		y_min = min(corner1.y, corner2.y)
		y_max = max(corner1.y, corner2.y)
		for edge in self.edges:
			if edge.is_cutting_edge(Edge(Tile(x_min, y_min), Tile(x_max, y_min))) or \
			   edge.is_cutting_edge(Edge(Tile(x_min, y_max), Tile(x_max, y_max))) or \
			   edge.is_cutting_edge(Edge(Tile(x_min, y_min), Tile(x_min, y_max))) or \
			   edge.is_cutting_edge(Edge(Tile(x_max, y_min), Tile(x_max, y_max))):
				return False
		return self.is_contained(corner1, corner2)

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
	input_file = "Day9/input"
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