import numpy as np 
import pandas as pd

first_trial_cyclist =[10,15,12,18]
second_trial_cyclist=[12,11,21,24]

cyclist_trails =np.array([[10,15,12,18], [12,11,21,24]])
#print(type(cyclist_trails))

for i in cyclist_trails:
    for j in i:
        print(j)
    print(type(i))
    print(i)

print(cyclist_trails[0][2])
"""we have got two single dimensional arrays"""
# lets try to understand the boolean array 
test_scores=np.array([[83,71,57,63],[54,68,81,45]])
#this is a two dimensional array 
passing_score= test_scores>60
print (passing_score)
print (test_scores[passing_score])


        
    





