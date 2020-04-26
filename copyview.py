import numpy as np 
nyc_borough=np.array(["manhattan","queen", "broklyn", "bronx"])

print(nyc_borough)
borough_in_nyc=nyc_borough
print(id(nyc_borough))
print(id(borough_in_nyc))
