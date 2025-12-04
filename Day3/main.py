
import time

def get_joltage_rec_fast(line, start, digits, acum):
	if digits == 0: 
		return acum
	max_value = 0
	max_index = start
	while digits <= len(line) - start:
		if int(line[start]) > max_value:
			max_value = int(line[start])
			max_index = start
		start += 1
	return get_joltage_rec_fast(line, max_index + 1, digits - 1, acum * 10 + max_value)

def get_joltage_fast(line, digits):
	return get_joltage_rec_fast(line, 0, digits, 0)

def get_max_joltage_rec_slow(line, start, digits, acum):
	if len(line) - start < digits:
		return 0
	elif digits == 0 or start >= len(line):
		return acum
	return max(
		get_max_joltage_rec_slow(line, start + 1, digits - 1, acum * 10 + int(line[start])),
		get_max_joltage_rec_slow(line, start + 1, digits, acum)
  )

def get_joltage_slow(line, digits):
	return get_max_joltage_rec_slow(line, 0, digits, 0)

def process_line(line, function, digits, line_num, total_lines):
	time_start_line = time.time()
	result = function(line, digits)
	print(f"\rProcessed line {line_num}/{total_lines} | Took {time.time() - time_start_line:.4f}s", end="")
	return result

def process_all_lines(lines, function, algo_name, digits):
	acum = 0
	total_lines = len(lines)
	print(f"Starting processing all lines using {algo_name}...")
	time_start = time.time()
	for i, line in enumerate(lines):
		acum += process_line(line.strip(), function, digits, i + 1, total_lines)
	print("\n")
	time_end = time.time()
	print(f"Total sum of wrong IDs ({algo_name}): {acum}")
	print(f"{algo_name} algorithm took {(time_end - time_start):.4f}s\n")
	return acum

def main():
	acum = 0
	input_file = "Day3/test"
	# input_file = "Day 2/test"
	with open(input_file, "r") as file:
		lines = list(file.readlines())
	process_all_lines(lines, get_joltage_fast, "Greedy", 12)
	process_all_lines(lines, get_joltage_slow, "Backtracking", 12)
if __name__ == "__main__":
	main()