#copy the contents of hello2.txt  to hello3.txt

file1=open("hello2.txt","r")
file2=open("hello3.txt","w")

for i in file1:
    file2.write(i)
    

file2.close()
file1.close()