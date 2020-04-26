import numpy as np 
distance =[20,30,40]
time=[2,3,4]
np_distance=np.array(distance)
np_time=np.array(time)
speed=np_distance / np_time
print(type(speed))
print(speed)

print ("The dimensions are ", np_distance.ndim)

print ("The shape of the array is:", np_distance.shape)
print ("The distance of the aary is:", np_distance.size)
print (" The dtype is:", np_distance.dtype)
