def operate_column(matrix, row, wide, height):
	operator = matrix[height - 1][row]
	print("operator is", operator)
	acum = 0 if operator == '+' else 1
	for i in range(height - 1):
		if operator == '+':
			acum += int(matrix[i][row])
		elif operator == '*':
			acum *= int(matrix[i][row])
		print(f"Operating {matrix[i][row]}")
	print(f"First column result is: {acum}")
	return acum

def main():
	acum = 0
	input_file = "Day6/input"
	with open(input_file, "r") as file:
		lines = list(file.readlines())
	matrix = list(map(lambda x: x.split(), lines))
	print(matrix)
	wide = len(matrix[0])
	height = len(matrix)
	print(f"Matrix with dimensions: {height}, {wide}")
	for i in range(wide):
		acum += operate_column(matrix, i, wide, height)
	print(f"Final result is: {acum}")
	
if __name__ == "__main__":
	main()