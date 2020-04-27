#lets play with numpy

import numpy as np 
import matplotlib.pyplot as plt 
A=[12,34,45,56]
B=np.array(A)

print(type(B))
print(B)

print(B.size)
print(B.ndim)
print(B.shape)
print(B.dtype)

B[0]=100
print(B)

#slicing can be done 
#vector addition can be done 

C=A+B
print(C)
#numpy code will run super fast 

#normal multiplication and vector multiplication is possible 1:1 multiply 

D=C*2
print(D)

E=D*B
print(E)

F=np.dot(A,B)
print(F)

#broadcasting

G=B+2 
print(G)

#lot of functions like mean 
H=B.mean()
print(H)
I=B.max()
print(I)
J=B.min()
print(J)

#we can use pi, sin,linspace

print(np.linspace(-2,2,5))

z=(plt.plot(B,C))
plt.imshow(z)
