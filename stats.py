import numpy as np 
from scipy.stats import norm 
import matplotlib.pyplot as plt 

rvs=norm.rvs(loc=0,scale=1, size=100)


plt.plot(rvs)
plt.show()

plt.hist(rvs,density=True)
plt.show()
