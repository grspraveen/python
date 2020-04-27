#lets play with 2D

import numpy as np 
A=[[12,34,45],[45,56,67], [10,20,30]]
print(A)
B=np.array(A)
print(B)

print("The number of dimensions are",B.ndim)
print("The shape of the array is",B.shape)
print("The size of the array is",B.size)
print(B[2][2])

#this is for matrix addition 

C=B+B
print(C)

D=2*C
print(D)

#matrix multiplicaiton can be done with help of dot

E=np.dot(B,B)
print(E)