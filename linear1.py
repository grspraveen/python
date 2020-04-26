import numpy as np 
from scipy import linalg

# Let us try to find the solution of three linear equations with three variables. 
# 2x + 3y + z = 21 -- (1) -x + 5y + 4z = 6 -- (2) 3x + 2y + 9z = 6 -- (3)

coff_array=np.array([[2,3,1],[-1,5,4],[3,2,9]])
value_array=np.array([21,9,6])

print(linalg.solve(coff_array,value_array))