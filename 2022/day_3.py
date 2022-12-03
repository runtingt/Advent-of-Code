# Imports
from aocd import get_data, submit

# Get data
data = get_data(day=3, year=2022).split('\n')

##### Part 1 ######
# Split into rucksacks with two compartments
rucksacks = [[string[0:len(string)//2], string[len(string)//2:]] for string in data]

# Get priorities of items in both compartments
priorities = []
for rucksack in rucksacks:
    in_both = list(set(rucksack[0]).intersection(set(rucksack[1])))[0]
    if in_both.islower():
        priorities.append(ord(in_both)-ord('a')+1)
    elif in_both.isupper():
        priorities.append(ord(in_both)-ord('A')+27)
submit(sum(priorities), part='a', day=3, year=2022)

##### Part 2 #####
# Group into lines of three
groups = [data[i:i+3] for i in range(0, len(data), 3)]

# Get the priorities of the items that appear in all three rucksacks
priorities = []
for group in groups:
    in_all = list(set(group[0]).intersection(set(group[1])).intersection(set(group[2])))[0]
    if in_all.islower():
        priorities.append(ord(in_all)-ord('a')+1)
    elif in_all.isupper():
        priorities.append(ord(in_all)-ord('A')+27)
submit(sum(priorities), part='b', day=3, year=2022)
