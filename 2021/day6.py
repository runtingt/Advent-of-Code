import numpy as np
import matplotlib.pyplot as plt

# Import the data
input = np.genfromtxt("C:/Users/tomru/Desktop/Python Playground/Advent of Code/2021/day6.txt",
                      dtype=int, delimiter=',')
input = np.array([3,4,3,1,2], dtype=int)

#### Part One ####
#print("Initial state {0}".format(input))
for i in range(1, 81):
    #print("Day {0}".format(i))
    # Subtract 1 and reset any timers
    input -= 1
    reset_indexes = np.where(input == -1)[0]
    input[reset_indexes] = 6
    
    # Spawn a new element if timer is zero
    for j in range(len(reset_indexes)):
        input = np.append(input, 8)
    
    # Print state
    #print("After {0} days: {1}".format(i, input))
    
print("Total fish: {0}".format(len(input)))

#### Part Two ####
input = np.genfromtxt("C:/Users/tomru/Desktop/Python Playground/Advent of Code/2021/day6.txt",
                      dtype=int, delimiter=',')

# We need a much faster method, so group the fish by frequency instead
num_fish = len(input)
freq, edges = np.histogram(input, bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#print("Initial state {0}".format(freq))
for i in range(1, 257):
    # Shift the array to the left
    freq = np.roll(freq, -1)
    # The fish with expired timers become new fish with timers of 8, 
    # so increase the number of fish at timer=6 by the number of new fish
    freq[6] += freq[-1]
    #print("After {0} days: {1}".format(i, freq))
    
print("Total fish: {0}".format(np.sum(freq)))

# Visualise data
fig, ax = plt.subplots(1, 1, figsize=(12,6))
ax.bar(edges[:-1], freq, width=np.diff(edges), edgecolor="black")
ax.set_xticks(edges[:-1])
