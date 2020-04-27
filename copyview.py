import numpy as np 
nyc_borough=np.array(["manhattan","queen", "broklyn", "bronx"])

print(nyc_borough)
borough_in_nyc=nyc_borough
print(id(nyc_borough))
print(id(borough_in_nyc))

view_borough_in_nyc=borough_in_nyc
borough_in_nyc[3]="praveen"
print()