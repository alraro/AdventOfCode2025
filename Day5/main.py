def parse_input(lines):
	divider = lines.index("\n")
	ranges = lines[:divider]
	ingredients = lines[divider+1:]
	ranges = list(map(lambda x: x.strip(), ranges))
	ingredients = list(map(lambda x: x.strip(), ingredients))
	return ranges, ingredients

def is_fresh(ingredient, ranges):
	ingredient = int(ingredient)
	for range in ranges:
		left, right = range.split('-')
		if ingredient >= int(left) and ingredient <= int(right):
			return True
	return False

def main():
	acum = 0
	input_file = "Day5/input"
	with open(input_file, "r") as file:
		lines = list(file.readlines())
	ranges, ingredients = parse_input(lines)
	for ingredient in ingredients:
		if is_fresh(ingredient, ranges):
			acum += 1
	print(f"Total fresh items are: {acum}")
if __name__ == "__main__":
	main()