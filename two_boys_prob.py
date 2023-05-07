#probability of having 2 boys out of 4 children

import itertools
sample_space = list(itertools.product("BG", repeat=4))
#print(sample_space)
count=0
for i in sample_space:
    boys=i.count("B")
    if boys==2:
        count+=1
    
    
probability=count/len(sample_space)
print("Probability of 2 boys is: ",round(probability,3))
        
