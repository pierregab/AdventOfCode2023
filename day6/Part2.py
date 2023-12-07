with open(file_path, 'r', encoding='utf-16') as file:
    lines = file.readlines()

# Parsing the input as a single race
time = int(''.join(lines[0].strip().split()[1:]))
distance_record = int(''.join(lines[1].strip().split()[1:]))

# Calculate the number of ways to win for the single race in the actual puzzle input
ways_to_win_single_race_actual = calculate_ways_to_win(time, distance_record)

print(ways_to_win_single_race_actual)
