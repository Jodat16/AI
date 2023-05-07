#Let A be the event that an even number turns up and let B be the event that a number
#divisible by 3 occurs. Find P (A ∪ B) and P (A ∩ B).

sample_space = list(range(1, 7))
event_A = [2, 4, 6]
event_B = [3, 6]

prob_union = len(set(event_A) | set(event_B)) / len(sample_space) #union=|

prob_intersection = len(set(event_A) & set(event_B)) / len(sample_space) #intersection=&

# Print the probabilities of the union and intersection of events A and B
print("Probability of A union B:", prob_union)
print("Probability of A intersection B:", prob_intersection)

# check=set(event_A) & set(event_B)
# print(check) output 6
