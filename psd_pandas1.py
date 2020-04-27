import pandas as pd 
import pandas as pd1

df=pd.read_csv("covid1.csv")
print(df.head())

#read excel sheet 
#you need to install xlrd to get the data from excel 

df1=pd1.read_excel("employee.xlsx")
print(df1.head())
print(df1)