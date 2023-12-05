def calculate_total_scratchcards_max_optimized(file_path):
    with open(file_path, 'r', encoding='utf-16') as file:
        lines = file.readlines()

    # Parsing the lines into winning and owned numbers
    cards = []
    for line in lines:
        parts = line.strip().split(' | ')
        if len(parts) != 2:
            continue
        winning_numbers = set(map(int, parts[0].split()[2:]))
        owned_numbers = list(map(int, parts[1].split()))
        cards.append((winning_numbers, owned_numbers))

    # Pre-computing the number of matches for each card
    matches_count = [sum(1 for num in owned if num in winning) for winning, owned in cards]

    # Using cumulative sums to calculate total instances
    total_instances = [1] * len(cards)  # Start with 1 instance of each card
    for index in range(len(cards) - 2, -1, -1):  # Start from the second last card
        total_instances[index] += sum(total_instances[index + 1:index + 1 + matches_count[index]])

    # Sum of all instances gives the total number of scratchcards
    total_scratchcards = sum(total_instances)

    return total_scratchcards

# Replace 'file_path' with the path to your file
total_scratchcards = calculate_total_scratchcards_max_optimized('AOC4.txt')
print(total_scratchcards)
