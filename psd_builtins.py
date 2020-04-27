#lets try to evaluate some builtin functions 


A=[12,34,45,55,34.44,67,77,45.11]

print(sum(A))
print(len(A))
print(sorted(A))

#if you put A.sort() the list gets changed. with "sorted", the list doesnt get changed 

def nowork():
    pass

c=nowork()
print(c)