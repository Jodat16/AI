import itertools

num_white = 10
num_red = 20
num_green = 30

# create the sample space by generating all possible combinations of 5 balls
sample_space  = list(itertools.product("WRG", repeat=5)) #only used it it says with replacement
#print(sample_space)

count = 0
for outcome in sample_space:
    num_white_outcome = outcome.count('W') #count presence of a specifc element in a tuple or list
    num_red_outcome = outcome.count('R')
    if num_white_outcome == 3 or num_red_outcome == 2:
        count += 1


probability = count / len(sample_space)

# print the probability
print("The probability of getting 3 white balls or 2 red balls when drawing 5 balls with replacement is:", probability)

count = 0
for outcome in sample_space:
    num_white_outcome = outcome.count('W') #count presence of a specifc element in a tuple or list
    num_red_outcome = outcome.count('R')
    num_green_outcome = outcome.count('G')
    if num_white_outcome == 5 or num_red_outcome == 5 or num_green_outcome==5:
        count += 1
        
print("The probability of getting all 5 balls of same color with replacement is:", probability)

# if it says without replacement
'''
import itertools
sample_space = list(itertools.combinations("B"*5 + "G"*7, 4))
#print(sample_space)
print(len(sample_space))'''

'''In this code, we're using the itertools.combinations function to generate all possible combinations of 
4 balls that can be drawn from a box containing 5 black (B) and 7 green (G) balls without replacement.'''
