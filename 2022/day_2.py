# Imports
from aocd import get_data, submit

# Get data
data = get_data(day=2, year=2022).split('\n')

# Part 1
score = 0
for line in data:
    # Rock
    if line[0] == 'A':
        if line[-1] == 'X':
            score += 1 # Rock
            score += 3 # Draw
        elif line[-1] == 'Y':
            score += 2 # Paper
            score += 6 # Win
        elif line[-1] == 'Z':
            score += 3 # Scissors
    # Paper
    elif line[0] == 'B':
        if line[-1] == 'Y':
            score += 2 # Paper
            score += 3 # Draw
        elif line[-1] == 'Z':
            score += 3 # Scissors
            score += 6 # Win
        elif line[-1] == 'X':
            score += 1 # Rock
    # Scissors
    if line[0] == 'C':
        if line[-1] == 'Z':
            score += 3 # Scissors
            score += 3 # Draw
        elif line[-1] == 'X':
            score += 1 # Rock
            score += 6 # Win
        elif line[-1] == 'Y':
            score += 2 # Paper
submit(score, part='a', day=2, year=2022)

# Part two
score = 0
for line in data:
    # Rock
    if line[0] == 'A':
        if line[-1] == 'X': # Lose
            score += 3 # Scissors
            score += 0 # Lose
        elif line[-1] == 'Y': # Draw
            score += 1 # Rock
            score += 3 # Draw
        elif line[-1] == 'Z': # Win
            score += 2 # Paper
            score += 6 # Win
    # Paper
    if line[0] == 'B':
        if line[-1] == 'X': # Lose
            score += 1 # Rock
            score += 0 # Lose
        elif line[-1] == 'Y': # Draw
            score += 2 # Paper
            score += 3 # Draw
        elif line[-1] == 'Z': # Win
            score += 3 # Scissors
            score += 6 # Win
    # Scissors
    if line[0] == 'C':
        if line[-1] == 'X': # Lose
            score += 2 # Paper
            score += 0 # Lose
        elif line[-1] == 'Y': # Draw
            score += 3 # Scissors
            score += 3 # Draw
        elif line[-1] == 'Z': # Win
            score += 1 # Rock
            score += 6 # Win
submit(score, part='b', day=2, year=2022)
