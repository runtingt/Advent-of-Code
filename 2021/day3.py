import numpy as np

# Load the data
input = np.loadtxt("C:/Users/tomru/Desktop/Python Playground/Advent of Code/2021/day3.txt",
                   dtype="U12")

#### Part One ####
# Get the most and least common bits at each position
gamma_rate = ""
epsilon_rate = ""
for i in range(len(input[0])):
    bit = np.vectorize(lambda s: int(s[i]))(input)
    most_common = np.bincount(bit).argmax()
    least_common = np.bincount(bit).argmin()
    gamma_rate += str(most_common)
    epsilon_rate += str(least_common)
    
# Convert to decimal
gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

print(gamma_rate * epsilon_rate)

#### Part Two ####
test = np.array(["00100","11110","10110","10111","10101","01111","00111","11100","10000",
                 "11001","00010","01010"], dtype="U5")

# Sort on most common bits
i = 0
input_to_sort = np.unique(input)
while(len(input_to_sort) > 1):
    bit = np.vectorize(lambda s: s[i])(input_to_sort)
    count = np.bincount(bit.astype(np.int8))
    if(count[0] == count[1]):
        accepted = np.where(bit == "1")
    else:
        accepted = np.where(bit == str(count.argmax()))
    input_to_sort = input_to_sort[accepted]
    i += 1
    #print(input_to_sort)
    
# Convert to decimal
oxygen_rating = int(input_to_sort[0], 2)

# Sort on least common bits
i = 0
input_to_sort = np.unique(input)
while(len(input_to_sort) > 1):
    bit = np.vectorize(lambda s: s[i])(input_to_sort)
    count = np.bincount(bit.astype(np.int8))
    if(count[0] == count[1]):
        accepted = np.where(bit == "0")
    else:
        accepted = np.where(bit == str(count.argmin()))
    input_to_sort = input_to_sort[accepted]
    i += 1
    #print(input_to_sort)
    
# Convert to decimal
co2_rating = int(input_to_sort[0], 2)

# Get life support rating
print(oxygen_rating, co2_rating, oxygen_rating*co2_rating)