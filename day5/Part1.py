def parse_input(input_text):
    sections = input_text.split('\n\n')
    seeds = [int(seed) for seed in sections[0].split(': ')[1].split()]
    maps = {}
    for section in sections[1:]:
        lines = section.split('\n')
        map_name = lines[0].split(' map:')[0].replace('-', '_')
        map_values = [list(map(int, line.split())) for line in lines[1:]]
        maps[map_name] = map_values
    return seeds, maps

def apply_map(source_number, mapping):
    for destination_start, source_start, range_length in mapping:
        if source_start <= source_number < source_start + range_length:
            return destination_start + (source_number - source_start)
    return source_number

def find_locations(seeds, maps):
    location_numbers = []
    for seed in seeds:
        current_number = seed
        for map_type in ['seed_to_soil', 'soil_to_fertilizer', 'fertilizer_to_water', 
                         'water_to_light', 'light_to_temperature', 'temperature_to_humidity', 'humidity_to_location']:
            current_number = apply_map(current_number, maps[map_type])
        location_numbers.append(current_number)
    return location_numbers

def main():
    file_path = 'AOC5.txt'
    with open(file_path, 'r', encoding='utf-16') as file:
        puzzle_input = file.read()
    
    seeds, maps = parse_input(puzzle_input)
    location_numbers = find_locations(seeds, maps)
    lowest_location_number = min(location_numbers)
    print(f"The lowest location number is: {lowest_location_number}")

if __name__ == "__main__":
    main()
