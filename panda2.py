#handling missing values using pandas

import pandas as pd

first_series = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(first_series)

second_series = pd.Series([10,20,30,40,50],index=['c','e','f','g','h'])
print(second_series)

print("the sum of the series is ")
sum_of_series=first_series+ second_series
print(sum_of_series)

## Drop all the entires with NaN

dropna_s = sum_of_series.dropna()
print(dropna_s)

#fill all NaN with zeros
print("filling the NaN values with Zero")
fill_with_zero=sum_of_series.fillna(0)
print(fill_with_zero)




