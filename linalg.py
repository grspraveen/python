# inverse of a matrix using scipy 

import numpy as np 
from scipy import linalg
matrix=np.array([[10,6],[2,7]])
print(matrix)
type(matrix)
print(type(matrix))
print(linalg.inv(matrix))

#find the determinant of the matrix'

matrix1=np.array([[4,9],[3,5]])
print(matrix1)
print(linalg.det(matrix1))


