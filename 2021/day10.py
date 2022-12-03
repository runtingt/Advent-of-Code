import numpy as np

# Load the data
data = np.genfromtxt("day10.txt", dtype=str, delimiter='\n')
# =============================================================================
# data = np.array(["[({(<(())[]>[[{[]{<()<>>",
#                 "[(()[<>])]({[<{<<[]>>(",
#                 "{([(<{}[<>[]}>{[]{[(<()>",
#                 "(((({<>}<{<{<>}{[]{[]{}",
#                 "[[<[([]))<([[{}[[()]]]",
#                 "[{[{({}]{}}([{[{{{}}([]",
#                 "{<[[]]>}<{[{[{[]{()[[[]",
#                 "[<(<(<(<{}))><([]([]()",
#                 "<{([([[(<>()){}]>(<<{{",
#                 "<{([{{}}[<[[[<>{}]]]>[]]"])
# =============================================================================

# Define the corresponding opening and closing characters and their penalties
opening_chars = np.array(["(", "[", "{", "<"])
closing_chars = np.array([")", "]", "}", ">"])
penalty_points = {")" : 3, "]" : 57, "}" : 1197, ">" : 25137}
autocomplete_points = {")" : 1, "]" : 2, "}" : 3, ">" : 4}


#### Part One ####
# Iterate through each line
illegal_chars = np.empty(0)
incomplete_chunks = np.empty(0) # For use in Part Two
for line in data:
    open_chunks = np.empty(0)
    is_corrupted = False
    for symbol in line:
        # If opening character, append to list of open chunks
        if symbol in opening_chars:
            open_chunks = np.append(open_chunks, symbol)
        # If closing character, check it is the correct character for that chunk
        else:
            expected = closing_chars[np.where(opening_chars == open_chunks[-1])][0]
            if symbol == expected:
                open_chunks = np.delete(open_chunks, -1)
            else:
                #print("Expected {0} but found {1}".format(expected, symbol))
                illegal_chars = np.append(illegal_chars, symbol)
                is_corrupted = True
                break # Stop at the first incorrect character
    # If we make it all the way through, the line is just incomplete
    if not is_corrupted:
        incomplete_chunks = np.append(incomplete_chunks, 
                                      ''.join(open_chunks)) # For use in Part Two

# Calculate the total penalty points:
penalties = 0
for symbol in illegal_chars:
    penalties += penalty_points[symbol]
print("Total penalty points: {0}".format(penalties))

#### Part Two ####
scores = np.empty(0, dtype=int)
for line in incomplete_chunks:
    score = 0
    for symbol in reversed(line):
        # Get corresponding closing character
        char_to_close = closing_chars[np.where(opening_chars == symbol)][0]
        # Update score
        score *= 5
        score += autocomplete_points[char_to_close]
    scores = np.append(scores, score)
print("Middle score: {0:.0f}".format(np.median(scores)))
