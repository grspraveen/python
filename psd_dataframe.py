#lets create a data frame 
import pandas as pd 
employee={"employee number":[1,2,3,4,5],
        "employee name": ["Prameela","Aneela","Srujan", "Ranjith", "srikanth"],
        "salary": [2000,3000,4000,5000,6000]}

print(employee)

df=pd.DataFrame(employee)
print(df)

y=df[["employee name"]]
print(y)

z=df.iloc[0,0]
print(z)

x=df.iloc[0:2,0:2]
print(x)
