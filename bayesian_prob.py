''' QUES
A manufacturing firm employs three analytical plans for the design and development of a
particular product. For cost reasons, all three are used at varying times. In fact, plans 1, 2,
and 3 are used for 30%, 20%, and 50% of the products, respectively. The defect rate is
different for the three procedures as follows: P(D|P1)=0.01, P(D|P2)=0.03, P(D|P3)=0.02,
where P(D|Pj ) is the probability of a defective product, given plan j. If a random product was
observed and found to be defective, which plan was most likely used and thus responsible?
'''

prob_P1 = 0.3
prob_P2 = 0.2
prob_P3 = 0.5

prob_D_given_P1 = 0.01 #P(D|P1)
prob_D_given_P2 = 0.03
prob_D_given_P3 = 0.02


prob_D = prob_P1 * prob_D_given_P1 + prob_P2 * prob_D_given_P2 + prob_P3 * prob_D_given_P3

prob_P1_given_D = (prob_P1 * prob_D_given_P1) / prob_D
prob_P2_given_D = (prob_P2 * prob_D_given_P2) / prob_D
prob_P3_given_D = (prob_P3 * prob_D_given_P3) / prob_D

max_prob = max(prob_P1_given_D, prob_P2_given_D, prob_P3_given_D)
if max_prob == prob_P1_given_D:
    print("Plan 1 is most likely responsible.")
elif max_prob == prob_P2_given_D:
    print("Plan 2 is most likely responsible.")
else:
    print("Plan 3 is most likely responsible.")
