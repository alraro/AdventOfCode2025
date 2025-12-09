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


class Board:
	def __init__(self):
		self.tiles = []
		self.count = 0
  
	def add_tile(self, tile):
		self.tiles.append(tile)
		self.count += 1
  
	def get_tile(self, index):
		return self.tiles[index]

	def is_inside(self, corner1, corner2):
		x_min = min(corner1.x, corner2.x)
		x_max = max(corner1.x, corner2.x)
		y_min = min(corner1.y, corner2.y)
		y_max = max(corner1.y, corner2.y)
		for tile in self.tiles:
			if x_min <= tile.x <= x_max and y_min <= tile.y <= y_max:
				return True
		return False
 
def main():
	board = Board()
	biggest = 0
	input_file = "Day9/input"
	with open(input_file, "r") as file:
		lines = list(file.readlines())
	for line in lines:
		line = line.strip()
		x, y = line.split(",")
		x = int(x)
		y = int(y)
		board.add_tile(Tile(x, y))
	i = 0
	while i < board.count - 1:
		curr = board.get_tile(i)
		j = i + 1
		while j < board.count:
			other = board.get_tile(j)
			area = curr.get_area(other)
			biggest = max(biggest, area)
			j += 1
		i += 1
	print("Biggest area:", biggest)
if __name__ == "__main__":
	main()