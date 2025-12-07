import functools



def main():
	res = 0
	has_changed = True
	input_file = "Day7/input"
	ouptput_file = "Day7/test_output_2"
	# input_file = "Day 2/test"
	with open(input_file, "r") as file:
		lines = list(file.readlines())
	
	lines = list(map(lambda x: x.strip('\n'), lines))
	width =  len(lines[0].strip())
	starting_pos = width // 2
	@functools.cache
	def get_divisions(x_start, y_start):
		height = len(lines)
		# print(f"Starting beam at {x_start}, {y_start}")
		if x_start < 0 or x_start >= len(lines[0]):
			# print(f"Invalid beam at {x_start}, {y_start}")
			return 1
		if y_start >= height:
			return 1
		if lines[y_start][x_start] == '^':
			# print("Found division ^ at ", x_start, y_start)
			left_divisions = get_divisions(x_start - 1, y_start)
			right_divisions = get_divisions(x_start + 1, y_start)
			# print(f"Left divisions: {left_divisions}, Right divisions: {right_divisions} at {y_start}, {x_start}")
			return left_divisions + right_divisions
		else:
			# lines[y_start] = lines[y_start][:x_start] + '|' + lines[y_start][x_start + 1:]
			return get_divisions(x_start, y_start + 1)
 
	res = get_divisions(starting_pos, 0)
	print(f"Final divisions are: {res}")
	
if __name__ == "__main__":
	main()