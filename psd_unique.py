#lets try unique using pandas

import pandas as pd 
df=pd.read_excel("employee.xlsx")
y=df["Team member"].unique()
print(y)

#some sort of sub table based on a condition df1=df[df["team member"]=="Praveen M"]

df2=df[df["Team member"]=="Praveen M"]
print(df2)

df2.to_csv("new list.csv")