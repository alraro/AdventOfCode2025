
def get_limits(id_range):
	split = id_range.split("-")
	start = int(split[0])
	end = int(split[1])
	return start, end

def is_repeated_twice(current_id):
	current_id_str = str(current_id)
	id_half = len(current_id_str) // 2
	first_half, second_half = current_id_str[:id_half], current_id_str[id_half:]
	if first_half == second_half:
		return True
	else:
		return False

def has_pattern(current_id):
	current_id_str = str(current_id)
	for index in range(1, len(current_id_str)):
		split_even = [current_id_str[j:j+index] for j in range(0, len(current_id_str), index)]
		if (len(set(split_even)) == 1):
			return True
	return False

def get_wrong_ids_inrange(start, end):
	acum = 0
	print(f"Calculating wrong IDs between {start} and {end}")
	for current_id in range(start, end + 1):
		if has_pattern(current_id):
			acum += current_id
	return acum

def main():
	acum = 0
	input_file = "Day2/input"
	# input_file = "Day 2/test"
	with open(input_file, "r") as file:
		lines = file.read()
	id_array = lines.split(",")
	for id_range in id_array:
		start, end = get_limits(id_range)
		acum += get_wrong_ids_inrange(start, end)
	print(f"Total sum of wrong IDs: {acum}")
if __name__ == "__main__":
	main()