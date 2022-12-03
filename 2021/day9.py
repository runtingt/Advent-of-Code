import numpy as np
import math

# Import data
data = np.genfromtxt("day9.txt", dtype='U100', delimiter='\n')
#data = np.array(["2199943210",
#                 "3987894921",
#                 "9856789892",
#                 "8767896789",
#                 "9899965678"])

#### Part One ####
# Function for finding nearest neighbours
def nearest_neighbours(matrix, row, col):
    nearest_neighbours = np.empty(0)
    if row > 0:
        nearest_neighbours = np.append(nearest_neighbours,
                                       int(matrix[row - 1][col]))
    if row < len(matrix)-1:
        nearest_neighbours = np.append(nearest_neighbours,
                                       int(matrix[row + 1][col]))
    if col > 0:
        nearest_neighbours = np.append(nearest_neighbours,
                                       int(matrix[row][col - 1]))
    if col < len(matrix[0])-1:
        nearest_neighbours = np.append(nearest_neighbours,
                                       int(matrix[row][col + 1]))
        
    return nearest_neighbours


# Find all the low points
low_points = np.empty(0, dtype=int)
for i in range(len(data)):
    for j in range(len(data[i])):
        if int(data[i][j]) < np.min(nearest_neighbours(data, i, j)):
            low_points = np.append(low_points, int(data[i][j]))

# Get the risk levels
risk_levels = low_points + 1
print("Total risk level: {0}".format(np.sum(risk_levels)))

#### Part Two ####
# Convert to a grid
grid = []
for element in data:
    grid.append(list(map(int, element)))
    
# Count the number of basins
groups = []
def count_groups(i, j):
    if (j < 0 or j >= len(grid) or i < 0 or i >= len(grid[0])
        or grid[j][i] == 9 or grid[j][i] == -1):
        return
    grid[j][i] = -1
    groups[len(groups)-1] += 1
    count_groups(i+1, j)
    count_groups(i-1, j)
    count_groups(i, j+1)
    count_groups(i, j-1)

# Count get the largest three basins
for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
        groups.append(0)
        count_groups(j, i)
print(math.prod(sorted(groups, reverse=True)[:3]))
