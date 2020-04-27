#how to work with strings

name="hello this is praveen"
print(name)
print(name[6])
print(name[-4])
print(name[4:10])
print(name[::2])
print(name[0:10:3])
print(len(name))

append=".. and he is best"
print(name+append)
print(3*name)

#escape sequence

name2="Praveen \n myra \n chandrika"
print(name2)

#lets see tab now

name3="praveen \t myra \t chandrika"
print(name3)

#if you want to place a backslash in your string then place \\ 

#to convert to upper

name4="lets see if this goes in upper"
name5=name4.upper()
print(name5)

name6=name4.replace("if","may")
print(name6)
#find is used to find the sub string 

