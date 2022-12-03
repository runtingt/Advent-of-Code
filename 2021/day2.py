import numpy as np

# Load the data
input = np.loadtxt("C:/Users/tomru/Desktop/Python Playground/Advent of Code/2021/day2.txt", 
                   dtype={"names" : ("command", "value"), "formats" : ("U10", "i4")})

#### Part One ####
# Count the amount forward
num_forward = np.ma.masked_where(input["command"] != "forward", input["value"])

# Count the amount up
num_up = np.ma.masked_where(input["command"] != "up", input["value"])

# Count the amount down
num_down = np.ma.masked_where(input["command"] != "down", input["value"])

# Calculate final value
print((np.sum(num_down) - np.sum(num_up)) * np.sum(num_forward))

#### Part Two ####
aim = 0
horizontal_position = 0
depth = 0
for index, entry in enumerate(input):
    command = entry["command"]
    value = entry["value"]
    
    if command == "forward":
       depth += value*aim
       horizontal_position += value
    elif command == "down":
        aim += value
    elif command == "up":
        aim -= value
    else:
        print("Invalid command")
print(depth*horizontal_position)
    