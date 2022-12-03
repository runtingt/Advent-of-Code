import numpy as np

# Get the input and separate points and instructions
inputs = np.loadtxt("day13.txt", dtype=str, delimiter="\n")
data = np.empty((0, 2))
instructions = np.empty(0)
for line in inputs:
    if line[0] != "f":
        data = np.vstack((data, line.split(",")))
    else:
        instructions = np.append(instructions, line)
data = data.astype(int)

# Test input
# =============================================================================
# data = np.array([[6,10],
#                  [0,14],
#                  [9,10],
#                  [0,3],
#                  [10,4],
#                  [4,11],
#                  [6,0],
#                  [6,12],
#                  [4,1],
#                  [0,13],
#                  [10,12],
#                  [3,4],
#                  [3,0],
#                  [8,4],
#                  [1,10],
#                  [2,14],
#                  [8,10],
#                  [9,0]])
# 
# instructions = ["fold along y=7","fold along x=5"]
# =============================================================================

#### Part One and Part Two ####
x_values = data[:, 0]
y_values = data[:, 1]
dimensions = (np.max(y_values)+1, np.max(x_values)+1)
grid = np.full(dimensions, 0)

# Add 1s where specified by the imported data
for element in data:
    grid[element[1]][element[0]] = 1
print("Initial grid\n{0}".format(grid))
   
# "Fold" the array
for instruction in instructions:# [0:1]: # Part one only requires the first fold
    instruction = instruction[11:]
    if instruction[0] == 'y':
        temp = np.empty((0, len(grid[0])))
        print("Fold along y-direction at y=", instruction[2:])
        index = 0
        # Perform the fold line by line
        for line in reversed(grid[int(instruction[2:])+1:]):
            folded_line = np.logical_or(line, grid[index]).astype(int)
            temp = np.vstack((temp, folded_line))
            index += 1
    if instruction[0] == 'x':
        temp = np.empty((0, len(grid[0])//2))
        print("Fold along x-direction at x=", instruction[2:])
        for line in grid:
            folded_line = np.logical_or(line[0:int(instruction[2:])], 
                                        line[int(instruction[2:])+1:][::-1]).astype(int)
            temp = np.vstack((temp, folded_line))
        
    # Assign grid to the folded version
    grid = temp
    print(grid)
    
num_ones = list(grid.flatten()).count(1)
print(num_ones)
