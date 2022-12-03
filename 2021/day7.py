import numpy as np

# Import the data
input_array = np.genfromtxt("C:/Users/tomru/Desktop/Python Playground/Advent of Code/2021/day7.txt",
                            dtype=int, delimiter=',')

#input_array = np.array([16,1,2,0,4,2,7,1,2,14])

#### Part One ####
# To minimise the distance each element must move, we just need the median
median = np.median(input_array)
distance_to_median = np.abs(input_array - median)
print("Total fuel spent: {0:.0f}".format(np.sum(distance_to_median)))

#### Part Two ####
# Moving is now more expensive further out, so we need the mean
# We use floor because reasons
mean = np.floor(np.mean(input_array))
distance_to_mean = np.abs(input_array - mean)

# Fuel spent per step follows 1+2+3+4+5+...+n, which sum has a closed form
fuel_spent = distance_to_mean*(distance_to_mean+1)/2
print("Total fuel spent: {0:.0f}".format(np.sum(fuel_spent)))