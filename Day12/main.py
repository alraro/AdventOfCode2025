
class Shape:
	def __init__(self, lines):
		self.id = int(lines[0].strip(":\n"))
		self.shape = []
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
		self.quantities = list(map(int, parts[1:]))
  
	def __str__(self):
		return f"Region {self.width}x{self.length} with quantities: {self.quantities}"

	def __repr__(self):
		return self.__str__()

def parse_input(lines):
	present_num = 6
	shapes = []
	regions = []
 
	while lines and present_num > 0:
		end = lines.index("\n") if "\n" in lines else len(lines)
		shapes.append(Shape(lines[:end]))
		lines = lines[end+1:]
		present_num -= 1
	
	for line in lines:
		if line.strip():
			regions.append(Region(line))
   
	return shapes, regions

def main():
	input_file = "Day12/test"
	
	with open(input_file, "r") as file:
		lines = list(file.readlines())

	shapes, regions = parse_input(lines)
 


if __name__ == "__main__":
	main()