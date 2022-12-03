import numpy as np

# Load the data
input = np.loadtxt("C:/Users/tomru/Desktop/Python Playground/Advent of Code/2021/day5.txt", 
                   dtype={"names" : ("pos1", "arrow", "pos2"), 
                          "formats" : ("U10", "U10", "U10")})

pos1 = np.char.split(input['pos1'], sep=',')
pos2 = np.char.split(input['pos2'], sep=',')

# =============================================================================
# pos1 = np.array([['0','9'],['8','0'],['9','4'],['2','2'],['7','0'],['6','4'],
#                  ['0','9'],['3','4'],['0','0'],['5','5']])
# pos2 = np.array([['5','9'],['0','8'],['3','4'],['2','1'],['7','4'],['2','0'],
#                  ['2','9'],['1','4'],['8','8'],['8','2']])
# =============================================================================

#### Part One ####
# Find the vents
vents = np.zeros((1000, 1000))
for i in range(len(input)):
    # Get x and y shifts and the number of steps to take in what direction
    x1 = int(pos1[i][0])
    x2 = int(pos2[i][0])
    y1 = int(pos1[i][1])
    y2 = int(pos2[i][1])
    delta_x = x2 - x1
    delta_y = y2 - y1 
    x_direction = np.sign(delta_x)
    y_direction = np.sign(delta_y)
    num_steps = max(abs(delta_x), abs(delta_y)) # Assume that abs(gradient) = 1
    #print(pos1[i][0], pos1[i][1], pos2[i][0], pos2[i][1])
    
    # Populate the vents array if we only consider horizontal and vertical lines
    if(x_direction == 0 or y_direction == 0):
        #print("Straight", delta_x, delta_y)
        for j in range(num_steps+1):
            #print("({0},{1})".format(x1 + j*x_direction, y1 + j*y_direction))
            vents[y1 + j*y_direction][x1 + j*x_direction] += 1

# Get the number where at least two lines overlap
print(len(np.where(vents>=2)[0]))


#### Part Two ####
# Same as before, just allow diagonal lines
# Find the vents
vents = np.zeros((1000, 1000))
for i in range(len(input)):
    # Get x and y shifts and the number of steps to take in what direction
    x1 = int(pos1[i][0])
    x2 = int(pos2[i][0])
    y1 = int(pos1[i][1])
    y2 = int(pos2[i][1])
    delta_x = x2 - x1
    delta_y = y2 - y1 
    x_direction = np.sign(delta_x)
    y_direction = np.sign(delta_y)
    num_steps = max(abs(delta_x), abs(delta_y)) # Assume that abs(gradient) = 1
    #print(pos1[i][0], pos1[i][1], pos2[i][0], pos2[i][1])
    
    # Populate the vents array
    for j in range(num_steps+1):
        #print("({0},{1})".format(x1 + j*x_direction, y1 + j*y_direction))
        vents[y1 + j*y_direction][x1 + j*x_direction] += 1
            
# Get the number where at least two lines overlap
print(len(np.where(vents>=2)[0]))