import numpy as np

# Load the data
numbers = [15,62,2,39,49,25,65,28,84,59,75,24,20,76,60,55,17,7,93,69,32,23,44,81,8,67,41,
           56,43,89,95,97,61,77,64,37,29,10,79,26,51,48,5,86,71,58,78,90,57,82,45,70,11,
           14,13,50,68,94,99,22,47,12,1,74,18,46,4,6,88,54,83,96,63,66,35,27,36,72,42,98,
           0,52,40,91,33,21,34,85,3,38,31,92,9,87,19,73,30,16,53,80]
numbers = np.array(numbers)

cards = np.loadtxt("C:/Users/tomru/Desktop/Python Playground/Advent of Code/2021/day4.txt")
cards = np.reshape(cards, (100, 5, 5))

# =============================================================================
# cards = np.array([22, 13, 17, 11, 0, 8, 2, 23,  4, 24,21,  9, 14, 16,  7, 6, 10,  3, 18,
#                   5, 1, 12, 20, 15, 19, 3, 15,  0,  2, 22, 9, 18, 13, 17,  5,19,  8,  7,
#                   25, 23,20, 11, 10, 24,  4,14, 21, 16, 12,  6,14, 21, 17, 24,  4,10, 16,
#                   15,  9, 19,18,  8, 23, 26, 20,22, 11, 13,  6,  5, 2,  0, 12,  3,  7,])
# cards = np.reshape(cards, (3, 5, 5))
# numbers= [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
# =============================================================================


# Get the winning card    
is_winner = False
i = 0
winning_card = None
winning_numbers_index = None
is_row = None
card_masks = np.ma.masked_where(cards == numbers[0], cards).mask
while not is_winner:
    # Combine the mask with the next number
    next_number_mask = np.ma.masked_where(cards == numbers[i], cards).mask
    card_masks = np.ma.mask_or(card_masks, next_number_mask)
    # Iterate through each row/column in each card, look for a line of "True" values
    for index, mask in enumerate(card_masks):
        for j in range(len(mask)):
            if mask[j, :].all():
                print("Card", index, "Row", j)
                is_winner = True
                winning_card_index = index
                winning_numbers_index = j
                is_row = True
                break
            elif mask[:, j].all():
                print("Card", index, "Col", j)
                is_winner = True
                winning_card_index = index
                winning_numbers_index = j
                is_row = False
                break
    i += 1
    
# Print winning card
print(cards[winning_card_index])

# Sum the unmarked numbers
unmarked = np.setdiff1d(cards[winning_card_index], numbers[0:i])
    
# Return the score
score = np.sum(unmarked) * numbers[i-1]
print("Score: {0:.0f}\n".format(score))

#### Part Two ####
# Loop unitl the last card is finished
cards_temp = cards
i = 0
card_masks = np.ma.masked_where(cards_temp == numbers[0], cards_temp).mask
while len(cards_temp) >= 1:
    # Combine the mask with the next number
    next_number_mask = np.ma.masked_where(cards_temp == numbers[i], cards_temp).mask
    card_masks = np.ma.mask_or(card_masks, next_number_mask)
    
    # Iterate through each row/column in each card, look for a line of "True" values
    indexes_to_delete = np.empty(0, dtype=int)
    for index, mask in enumerate(card_masks):
        for j in range(len(mask)):
            if mask[j, :].all():
                indexes_to_delete = np.append(indexes_to_delete, index)
            elif mask[:, j].all():
                indexes_to_delete = np.append(indexes_to_delete, index)
                
    # Increase counter           
    i += 1
    
    # Delete required cards after each pass
    if len(indexes_to_delete) < len(cards_temp):
        indexes_to_delete = np.unique(indexes_to_delete)
        cards_temp = np.delete(cards_temp, indexes_to_delete, axis=0)
        card_masks = np.delete(card_masks, indexes_to_delete, axis=0)
    else:
        break
    
# Print winning card
print(cards_temp[0])

# Sum the unmarked numbers
unmarked = np.setdiff1d(cards_temp[0], numbers[0:i])
    
# Return the score
score = np.sum(unmarked) * numbers[i-1]
print("Score: {0:.0f}\n".format(score))
    