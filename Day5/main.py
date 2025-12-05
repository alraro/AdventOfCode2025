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

def get_fresh_ingredients(ranges, ingredients):
	acum = 0
	for ingredient in ingredients:
		if is_fresh(ingredient, ranges):
			acum += 1
	return acum

def get_all_fresh(ranges):
	intervals = []
	for r in ranges:
		left, right = map(int, r.split('-'))
		intervals.append((left, right))
	intervals.sort(key=lambda x: x[0])
 
	merged = []
	if not intervals:
		return 0
	current_start, current_end = intervals[0]
	for start, end in intervals[1:]:
		if start <= current_end:
			current_end = max(current_end, end)
		else:
			merged.append((current_start, current_end))
			current_start, current_end = start, end

	merged.append((current_start, current_end))

	total_count = 0
	for start, end in merged:
		total_count += end - start + 1
	return total_count
  
def main():
	input_file = "Day5/input"
	with open(input_file, "r") as file:
		lines = list(file.readlines())
	ranges, ingredients = parse_input(lines)
	ingredients_fresh = get_fresh_ingredients(ranges, ingredients)
	all_possible_fresh = get_all_fresh(ranges)
	print(f"Total fresh items are: {ingredients_fresh}")
	print(f"The max number of fresh items is: {all_possible_fresh}")
if __name__ == "__main__":
	main()