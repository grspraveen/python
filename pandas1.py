
import numpy, pandas
data=pandas.read_csv("covid19.csv", delimiter ="," )
age=numpy.array(data["age"])
death=numpy.array(data["death"])
recovered=numpy.array(data["recovered"])
print(data)