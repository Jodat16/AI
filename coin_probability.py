#Coin Probability (getting sum even or greater than 7 of two coins)

import random

num_trials = 1000000  # number of trials to run
count_even_or_gt7 = 0  # count of trials where total score is even or greater than 7

for i in range(num_trials):
    dice1 = random.randint(1, 6)  # roll first dice
    dice2 = random.randint(1, 6)  # roll second dice
    total_score = dice1 + dice2
    if total_score % 2 == 0 or total_score > 7:
        count_even_or_gt7 += 1

prob_even_or_gt7 = count_even_or_gt7 / num_trials
print("Estimated probability of getting an even total score or a total score greater than 7:", round(prob_even_or_gt7,3))
