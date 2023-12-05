def calculate_points(file_path):
    with open(file_path, 'r', encoding='utf-16') as file:
        lines = file.readlines()

    total_points = 0

    for line in lines:
        # Splitting the line into two parts: before and after the "|"
        parts = line.strip().split(' | ')
        if len(parts) != 2:
            continue

        # Extract winning numbers and owned numbers
        winning_numbers, owned_numbers = parts
        winning_numbers = set(map(int, winning_numbers.split()[2:]))  # Exclude 'Card' and card number
        owned_numbers = list(map(int, owned_numbers.split()))

        # Calculate points for the card
        points = 0
        for number in owned_numbers:
            if number in winning_numbers:
                points = 1 if points == 0 else points * 2

        total_points += points

    return total_points

# Calling the function with the file path
print(calculate_points('AOC4.txt'))
