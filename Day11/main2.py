from collections import defaultdict

class Graph:
	def __init__(self, connections=None):
		self.graph = defaultdict(set)

	def add_edge(self, u, v):
		self.graph[u].add(v)

	def get_neighbors(self, u):
		return self.graph[u]

	def get_connections(self, node, destination, visited=None):
		if visited is None:
			visited = {node}
		if node == destination:
			if "fft" in visited and "dac" in visited:
				return 1
			else:
				return 0
		ways = 0
		neighbors = self.get_neighbors(node)
		for neighbor in neighbors:
			if neighbor not in visited:
				visited.add(neighbor)
				ways += self.get_connections(neighbor, destination, visited)
				visited.remove(neighbor)
		return ways

	def __str__(self):
		result = ""
		for node, neighbors in self.graph.items():
			result += f"{node}: {', '.join(neighbors)}\n"
		return result

	def __repr__(self):
		return self.__str__()
	
def main():
	input_file = "Day11/test2"
	with open(input_file, "r") as file:
		lines = list(file.readlines())
	graph = Graph()
	for line in lines:
		line = line.strip()
		parts = line.split(":")
		node = parts[0].strip(":")
		connections = parts[1].strip().split(" ")
		for conn in connections:
			graph.add_edge(node, conn)
	print(graph)
	connections = graph.get_connections("svr", "out")
	print("Total connections:", connections)
 

if __name__ == "__main__":
	main()