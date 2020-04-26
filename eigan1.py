import numpy as np 
from scipy import linalg

test_data=np.array([[5,8],[7,9]])

eigan_values=linalg.eig(test_data)
print(eigan_values)

