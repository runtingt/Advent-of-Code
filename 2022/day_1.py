# Imports
import numpy as np
from aocd import get_data, submit

# Get data
data = get_data(day=1, year=2022)

# Part 1
calories = data.split('\n\n')
elf_calories = np.empty(len(calories))
for i, entry in enumerate(calories):
    elf_calories[i] = np.sum(np.asarray(entry.split('\n')).astype(np.int32))
elf_calories = np.sort(elf_calories)[::-1]
largest = int(elf_calories[0])
submit(largest, part='a', day=1, year=2022)

# Part 2
largest_three = int(np.sum(elf_calories[:3]))
submit(largest_three, part='b', day=1, year=2022)
