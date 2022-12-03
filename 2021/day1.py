import numpy as np

# Load the data
input = np.loadtxt("C:/Users/tomru/Desktop/Python Playground/Advent of Code/2021/day1.txt")

#### Part One ####
# Calculate the number of times the data increases
num_increases = 0
for i in range(len(input)):
    try:
        if(input[i] > input[i-1]):
            num_increases += 1
    except IndexError:
        continue

# Print results
print("Number of increases: {0}".format(num_increases))

#### Part Two ####
# Calculate the number of times the data increases in a sliding window
num_increases = 0
for i in range(len(input)):
    try:
        if(np.sum(input[i+1:i+4]) > np.sum(input[i:i+3])):
            num_increases += 1
            #print(*input[i+1:i+4], ":", np.sum(input[i+1:i+4]), ">", *input[i:i+3], ":", np.sum(input[i:i+3]))
        #else:
            #print(*input[i+1:i+4], ":", np.sum(input[i+1:i+4]), "<", *input[i:i+3], ":", np.sum(input[i:i+3]))
    except IndexError:
        pass

# Print results
print("Number of increases in a sliding window: {0}".format(num_increases))
