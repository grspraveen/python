#lets try set theory functions using sets and relevant methods and operators

A={12,34,45,56,57,78}
B={12,22,33,44,55,56}

#& is used to find the intersection 
C=A & B
print(C)

#union is used to find the union of two sets

D=A.union(B)
print(D)

#to know if A is subset of B 
print(A.issubset(B))