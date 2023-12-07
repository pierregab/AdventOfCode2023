# Re-reading the puzzle input and calculating the solution in a single code block

def calculate_ways_to_win(time, distance_record):
    ways_to_win = 0
    for hold_time in range(time):
        travel_time = time - hold_time
        distance = hold_time * travel_time
        if distance > distance_record:
            ways_to_win += 1
    return ways_to_win

# Reading the puzzle input
with open(file_path, 'r', encoding='utf-16') as file:
    lines = file.readlines()

# Parsing the input
times = [int(x) for x in lines[0].strip().split()[1:]]
distances = [int(x) for x in lines[1].strip().split()[1:]]

# Calculate the number of ways to win for each race and the total product
total_ways_to_win = 1
for time, record in zip(times, distances):
    ways = calculate_ways_to_win(time, record)
    total_ways_to_win *= ways

total_ways_to_win

