import numpy as np

data = np.array(["5483143223",
                 "2745854711",
                 "5264556173",
                 "6141336146",
                 "6357385478",
                 "4167524645",
                 "2176841721",
                 "6882881134",
                 "4846848554",
                 "5283751526"])

data = np.genfromtxt("day11.txt", dtype=str, delimiter='\n')

# Transform the data to an array of digits
data = np.array([[int(digit) for digit in line] for line in data])

# Function to get the nearest neighbours in a matrix
def nearest_neighbours(matrix, row, col):
    nearest_neighbours = np.empty(0)
    rows = np.empty(0, dtype=int)
    cols = np.empty(0, dtype=int)
    if row > 0:
        nearest_neighbours = np.append(nearest_neighbours, matrix[row - 1][col])
        rows = np.append(rows, row-1)
        cols = np.append(cols, col)
    if row < len(matrix)-1:
        nearest_neighbours = np.append(nearest_neighbours, matrix[row + 1][col])
        rows = np.append(rows, row+1)
        cols = np.append(cols, col)
    if col > 0:
        nearest_neighbours = np.append(nearest_neighbours, matrix[row][col - 1])
        rows = np.append(rows, row)
        cols = np.append(cols, col-1)
    if col < len(matrix[0])-1:
        nearest_neighbours = np.append(nearest_neighbours, matrix[row][col + 1])
        rows = np.append(rows, row)
        cols = np.append(cols, col+1)
    if row > 0 and col > 0:
        nearest_neighbours = np.append(nearest_neighbours, matrix[row - 1][col - 1])
        rows = np.append(rows, row-1)
        cols = np.append(cols, col-1)
    if row > 0 and col < (len(matrix[0])-1):
        nearest_neighbours = np.append(nearest_neighbours, matrix[row - 1][col + 1])
        rows = np.append(rows, row-1)
        cols = np.append(cols, col+1)
    if row < len(matrix)-1 and col < len(matrix[0])-1:
        nearest_neighbours = np.append(nearest_neighbours, matrix[row + 1][col + 1])
        rows = np.append(rows, row+1)
        cols = np.append(cols, col+1)
    if row < len(matrix)-1 and col > 0:
        nearest_neighbours = np.append(nearest_neighbours, matrix[row + 1][col - 1])
        rows = np.append(rows, row+1)
        cols = np.append(cols, col-1)
        
    return (rows, cols)

#### Part One ####
total_flashed = 0
print("Initial state:\n{0}".format(data))
for i in range(100):
    # Increase the energy level of each octopus by 1
    data += 1
    # Propagate the flash outwards
    has_flashed = np.full(data.shape, False)
    num_flashed = len(np.where(has_flashed == True)[0])
    num_flashed_temp = num_flashed+1
    while num_flashed != num_flashed_temp:
        num_flashed = len(np.where(has_flashed == True)[0])
        flash_rows = np.where(data > 9)[0]
        flash_cols = np.where(data > 9)[1]
        for j in range(len(flash_rows)):
            neighbour_rows, neighbour_cols = nearest_neighbours(data, flash_rows[j], 
                                                                flash_cols[j])
            for k in range(len(neighbour_rows)):
                if not has_flashed[(flash_rows[j], flash_cols[j])]:
                    data[(neighbour_rows[k], neighbour_cols[k])] += 1
            has_flashed[(flash_rows[j], flash_cols[j])] = True
        num_flashed_temp = len(np.where(data > 9)[0])

    # Reset
    total_flashed += len(np.where(has_flashed == True)[0])
    data[np.where(has_flashed == True)] = 0
    has_flashed = np.full(data.shape, False)    
    
    # Print
    if (i+1)%20 == 0:
        print("After {0} days:\n{1}".format(i+1, data))
    
print("Total flashes: {0}".format(total_flashed))

#### Part Two ####
# Reset data
data = np.genfromtxt("day11.txt", dtype=str, delimiter='\n')
data = np.array([[int(digit) for digit in line] for line in data])

# Loop until all elements change at the same step
total_flashed = 0
i = 0
print("Initial state:\n{0}".format(data))
while(total_flashed != data.size):
    # Increase the energy level of each octopus by 1
    data += 1
    # Propagate the flash outwards
    has_flashed = np.full(data.shape, False)
    num_flashed = len(np.where(has_flashed == True)[0])
    num_flashed_temp = num_flashed+1
    while num_flashed != num_flashed_temp:
        num_flashed = len(np.where(has_flashed == True)[0])
        flash_rows = np.where(data > 9)[0]
        flash_cols = np.where(data > 9)[1]
        for j in range(len(flash_rows)):
            neighbour_rows, neighbour_cols = nearest_neighbours(data, flash_rows[j], 
                                                                flash_cols[j])
            for k in range(len(neighbour_rows)):
                if not has_flashed[(flash_rows[j], flash_cols[j])]:
                    data[(neighbour_rows[k], neighbour_cols[k])] += 1
            has_flashed[(flash_rows[j], flash_cols[j])] = True
        num_flashed_temp = len(np.where(data > 9)[0])

    # Reset
    total_flashed = len(np.where(has_flashed == True)[0])
    data[np.where(has_flashed == True)] = 0
    has_flashed = np.full(data.shape, False)    
    
    # Print
    if (i+1)%20 == 0:
        print("After {0} days:\n{1}".format(i+1, data))
    
    i += 1
    
print("Days before synchronisation: {0}".format(i))
    