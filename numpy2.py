import numpy as np 

"""the below code is not supported using lists
distance = [10,20,30,40]
time =[2,3,4,4]
speeed =distance / time 
print(speed)

"""
#now lets use numpy to do this operation. this is called nd array 

distance = np.array([10,20,30,40])
time =np.array([2,3,4,4])

speed =distance / time 
print(speed)

#create a array with Zeros 

array1=np.zeros((3,3))
print(array1)

#create an array with ones 

array2=np.ones((4,4))
print(array2)

#create an array with random numbers / empties 

array3=np.empty((2,2))
print(array3)

#create an array with sequence numbers 

array4=np.arange(12)
print(array4)

#reshape above array. that is array4 

array5=array4.reshape(3,4)
print(array5)

#linspace to get interval between two points in an array 

array6=np.linspace(1,10,5)
print(array6)

#three dimensional array

array7=np.arange(1,28)
print(array7)
array8=array7.reshape(3,3,3)
print(array8)


#know the dimensions of few arrays defined earlier 

print("The number of dimensions of array 7 are : ", array7.ndim)
print("The nunber of dimensions of array 8 are : ", array8.ndim)

#know the shape of the array
print("The shape of array 7 is :", array7.shape)
print("The shape of array 8 is :", array8.shape)

#know the size of the array 

print("The size of the array8 is", array8.size)

#understand dtype

array9=np.array(["delhi","banglore","hyderabad","chennai"])
print(array9.dtype)








