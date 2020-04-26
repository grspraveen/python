#lets play with the lists


list1=[2,45,"praveen",(45,56), "myra", 45.55]
print(list1)

#slicing can be done for the lists

print(list1[3:5])
print(list1[::4]) #with the gap of 

#syntax of list is like [startpoint:endpoint:increment of]


list2=list1+ [99,999,"chandrika"]
print(list2)

#concatinating or appending to the list 
#type this-->dir(list) to get the methods available 

print(list2.extend([45,"pinkey"]))

#there is a method called as append but index would increment by 1 as its like adding a list inside list 


#checking the mutable property of the list

list2[0]="chandrika"
print(list2)

del(list2[1])
print(list2)

#let us try to understand the split function in the list 

text1="hello this is praveen from another planet in the solar system and it is mars"
list3=text1.split()
print(list3)

text2="hello this is, praveen from another, planet in the solar system, and it is mars"
list4=text2.split(",")
print(list4)

#we are aliasing here. what ever changes we do to list 2 will reflect to list 5
list5=list2
list2[0]="banana"
print(list2)
print(list5)

#cloning so that the changes dont reflect. cloning or copying is same. so, if you change list 2, it wont get reflected in list 6 


list6=list2[:]




