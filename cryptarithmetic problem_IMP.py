from itertools import permutations

def solve_cryptarithmetic(puzzle):
    # Extract the unique characters from the puzzle
    chars = set(char for word in puzzle for char in word)
    
    # Try all possible digit assignments to the characters
    for digits in permutations(range(10), len(chars)):
        if any(digit == 0 for digit in digits):
            continue  # Skip assignments that start with 0
        
        # Create a dictionary mapping characters to digits
        char_to_digit = {char: digit for char, digit in zip(chars, digits)}
        
        # Convert each word to its corresponding integer value
        values = [int(''.join(str(char_to_digit[char]) for char in word)) for word in puzzle]
        
        # Check if the sum of the values is equal to the target value
        if sum(values[:-1]) == values[-1]:
            # If the solution is found, return the dictionary of character-to-digit mappings
            return char_to_digit
    
    # If no solution is found, return None
    return None

# Test the function with the BASE + BALL = GAMES puzzle
puzzle = ['BASE', 'BALL', 'GAMES']
solution = solve_cryptarithmetic(puzzle)
if solution is not None:
    print('Solution:', solution)
    print('BASE =', ''.join(str(solution[char]) for char in 'BASE'))
    print('BALL =', ''.join(str(solution[char]) for char in 'BALL'))
    print('GAMES =', ''.join(str(solution[char]) for char in 'GAMES'))
else:
    print('No solution found')
