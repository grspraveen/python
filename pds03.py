#playing with tuples

sample1=("praveen",12, 45.56)
print(sample1)
print(type(sample1))
print(sample1[1])

#tuples have index, similar to that of strings 

#tuples can be added

sample2=("myra", "hello", 67)

sample3=sample1 + sample2 
print(sample3)

#slicing can be applied for tuples and similar to that of strings 

#find the length of the tuple

print(len(sample3))

#tuples are immutable. so use another tuple to do operations on this tuple

sample4=(34,45,56,33,31,44)
sample5=sorted(sample4)
print(sample5)

#tuple with in tuple. nested tuples

sample6=("praveen",45,56.44, ("hello", 12), 67)
print(sample6)
print(sample6[3])

#accessing the elements of a tuple which is inside tuple 

print(sample6[3][1])

#there can be tuple inside tuple inside tuple then i guess it looks like a tree ? 
