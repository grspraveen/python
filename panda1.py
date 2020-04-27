import numpy as np 
import pandas as pd 

#trying with lists 
#keep a note that "S" should be in capital for "series"


first_series=pd.Series(list("abcdefghijkl"))
print(type(first_series))
print(first_series)

#trying with ndarray -numpy 

india=np.array(["hyd","blore", "delhi","chennai"])
print(type(india))

country=pd.Series(india)
print(country)

#vector operations

first_vector=pd.Series([1,2,3,4], index=["a","b","c","d"])
second_vector=pd.Series([10,20,30,40], index=["a","b","c","d"])
print(first_vector+second_vector)

olympic_hosts = {'HostCity': ['London','Beijing','Athens','Sydney','Atlanta'],
                'Year':[2012,2008,2004,2000,1996],
                'No of participating countries':[205,204,201,200,197]}

print(type(olympic_hosts))
df_olympic_data_dict = pd.DataFrame(olympic_hosts)
print(df_olympic_data_dict)


