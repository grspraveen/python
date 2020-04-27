import numpy as np 
first_list=[10,15,12,18]
second_list=[12,11,21,24]
print (type(first_list))
np_first_list=np.array(first_list)
np_second_list=np.array(second_list)
sum_list=np_first_list | np_second_list
print("The sum is", sum_list)
