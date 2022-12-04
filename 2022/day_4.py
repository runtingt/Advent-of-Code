# Imports
import numpy as np
from aocd import get_data, submit

# Get data and group into pairs
data = get_data(day=4, year=2022).split('\n')
data = [line.split(',') for line in data]

##### Part 1 ######
# Get number of full overlaps
full_overlaps = 0
for pair in data:
    pair_sections = []
    # Get sections for each pair
    for elf in pair:
        bounds = np.asarray(elf.split('-'), dtype=np.int32)
        pair_sections.append(set(np.arange(bounds[0], bounds[1]+1)))
    # Sort by length of sections
    pair_sections = sorted(pair_sections, key=lambda s: len(s))
    # Check if subset
    if pair_sections[0].issubset(pair_sections[1]):
        full_overlaps += 1
submit(full_overlaps, part='a', day=4, year=2022)

##### Part 2 #####
# Get number of intersections
intersections = 0
for pair in data:
    pair_sections = []
    # Get sections for each pair
    for elf in pair:
        bounds = np.asarray(elf.split('-'), dtype=np.int32)
        pair_sections.append(set(np.arange(bounds[0], bounds[1]+1)))
    # Sort by length of sections
    pair_sections = sorted(pair_sections, key=lambda s: len(s))
    # Check if intersection
    if pair_sections[0].intersection(pair_sections[1]):
        intersections += 1
submit(intersections, part='b', day=4, year=2022)
