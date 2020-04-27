#here goes one way of reading the file but need to put close at the end 

print("The content is ")
file1=open("PACIS.txt","r")
file_content=file1.read()
print(file_content)
file1.close()


#this is another way of reading the file but close not required 

print("the content in another way is")
with open("PACIS.txt","r") as file2:
    file_content1=file2.read()
    print(file_content1)

#lets try this as well to read all lines

file3=open("PACIS.txt","r")
buffer=file3.readlines()
print(buffer)
file3.close()


#lets try for each line

#reading lines using for loop 
list1=[]
file4=open("PACIS.txt","r")
for i in file4:
    list1.append(i)
    print(i)
file4.close()

print("here goes the content in the list")
print(list1)


