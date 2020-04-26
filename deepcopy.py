import numpy as np 
india=np.array(["hyderabad","bangalore","chennai","delhi"])
copy_india=india.copy()

print(india)
print(copy_india)

copy_india[3]="mumbai"

print(india)
print(copy_india)



