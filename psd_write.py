#lets try to write the content on to file 

file1=open("hello1.txt","w")
file1.write("This is first line\n")
file1.write("This is second line\n")
file1.write("This is third line\n")
file1.close()

#lets try to write multiple lines at once 

file2=open("hello2.txt","w")
list1=["this is first line\n","this is second line\n","this is third line\n"]
for i in list1:
    file2.write(i)

file2.close()


#lets try to append content in file2

file3=open("hello2.txt","a")
file3.write("This is line 5\n")
file3.write("This is line 6\n")
file3.close()

