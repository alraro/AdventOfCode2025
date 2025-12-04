def get_surrounding(lines, i, j):
	count = 0
	for x in range (i-1, i+2):
		for y in range(j-1, j+2):
			if x < 0 or y < 0 or x >= len(lines) or y >= len(lines[i]):
				continue
			if lines[x][y] == '@' and not (x == i and y == j):
				count += 1
	return count

def is_movable(lines, i, j):
	if lines[i][j] != '@':
		return False
	if get_surrounding(lines, i, j) >= 4:
		return False
	else :
		return True

def main():
	acum = 0
	has_changed = True
	input_file = "Day4/input"
	# input_file = "Day 2/test"
	with open(input_file, "r") as file:
		lines = list(file.readlines())
	while(has_changed):
		print("Current state:")
		for line in lines:
			print(line.strip())
		has_changed = False
		for i in range (0, len(lines)):
			for j in range (0, len(lines[i])):
				if is_movable(lines, i, j):
					lines[i] = lines[i][:j] + 'x' + lines[i][j+1:]
					has_changed = True
					acum += 1
	print("Total rolls:", acum)
if __name__ == "__main__":
	main()