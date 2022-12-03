# Import
with open("day8.txt") as input_file:
    data = [line for line in input_file.read().strip().split('\n')]
    
#### Part One ####
# Find digits 1 (len 2), 4 (len 4), 7 (len 3), 8 (len 7) 
outputs = [line.split('|')[1].strip().split(' ') for line in data]
lengths_allowed = [2, 3, 4, 7]
total_found = 0

# Find the allowed lengths
for output in outputs:
    for digit in output:
        if len(digit) in lengths_allowed:
            total_found += 1

print("Found {0}".format(total_found))

#### Part Two ####
# Numbers 0, 6, 9 have length 6 and 4 is part of 9
# 1 will also be part of 0, else it's a 6
# Numbers 2, 3, 5 have length 5 and 1 is part of 3, 5 is part of 6,
# else it's a 2

# Get inputs and outputs
inputs = [line.split('|')[0].strip().split(' ') for line in data]
outputs = [line.split('|')[1].strip().split(' ') for line in data]

# Decode the inputs, then use this on the outputs
total_found = 0
for i in range(len(data)):
    # Map each known digit to a number with a dictionary
    digit_map = {}
    for digit in inputs[i]:
        if len(digit) == 2:
            digit_map[1] = digit
        elif len(digit) == 4:
            digit_map[4] = digit
        elif len(digit) == 3:
            digit_map[7] = digit
        elif len(digit) == 7:
            digit_map[8] = digit
            
    # Find the unknown digits
    for digit in inputs[i]:
        # Digits 0, 6, 9
        if len(digit) == 6:
            # 4 is a part of 9
            if set(digit_map[4]).issubset(set(digit)):
                digit_map[9] = digit
            # 1 is a part of 0
            elif set(digit_map[1]).issubset(set(digit)):
                digit_map[0] = digit
            else:
                digit_map[6] = digit
    # Pass through again as we need to find 6 before we find 5
    for digit in inputs[i]:
        # Digits 2, 3, 5
        if len(digit) == 5:
            # 1 is a part of 3
            if set(digit_map[1]).issubset(set(digit)):
                digit_map[3] = digit
            # 5 is a part of 6
            elif set(digit).issubset(set(digit_map[6])):
                digit_map[5] = digit
            else:
                digit_map[2] = digit
    
    # We know what the digits are for each line, now we decode the output
    number = []
    for digit in outputs[i]:
        for key, value in digit_map.items():
            if set(digit) == set(value): # Use sets as the order may change
                number.append(str(key))
    number = int(''.join(number))
    total_found += number

# Print the answer
print("Sum of digits: {0}".format(total_found))
