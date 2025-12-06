
def append_matrix_column(matrix):
	matrix.append([0])

def arr_to_int(arr):
	result = 0
	if len(set(arr)) == 1 and arr[0] == ' ':
		return -1
	for i in range(len(arr)):
		if (arr[i] == ' '):
			continue
		result = result * 10 + int(arr[i])
	return result

def get_operators(lines):
	operators = lines[-1].strip().split()
	return operators

def main():
	acum = 0
	number_matrix = []
	input_file = "Day6/input"
	with open(input_file, "r") as file:
		lines = list(map(lambda x: x.strip("\n"), file.readlines()))
	total_numbers = len(lines) - 1
	width = len(lines[0])
	
	all_digits = []
	for i in range(width):
		digits = [lines[x][i] for x in range(total_numbers)]
		all_digits.append(digits)
		
	all_digits = list(map(arr_to_int, all_digits))
	# print(f"The numbers are: {all_digits}")
	operators = get_operators(lines)
	# print(f"The operators are: {operators}")
	
	for operator in operators:
		# print(f"Current operator: {operator}")
		if operator == '+':
			# print(f"Adding {all_digits[0]} to acum {acum}")
			temp = 0
			i = 0
			while i < len(all_digits) and all_digits[i] != -1:
				temp += all_digits[i]
				i += 1
			all_digits = all_digits[i+1:]
			operators = operators[1:]
			# print(f"Temp sum is: {temp}, remaining digits: {all_digits}, remaining operators: {operators}")
			acum += temp
		elif operator == '*':
			# print("Processing multiplication")
			temp = 1
			i = 0
			while i < len(all_digits) and all_digits[i] != -1:
				temp *= all_digits[i]
				i += 1
			all_digits = all_digits[i+1:]
			operators = operators[1:]
			acum += temp
		else:
			print(f"Unknown operator {operator}, skipping")
			operators = operators[1:]
	print(f"The final result is: {acum}")
	
if __name__ == "__main__":
	main()