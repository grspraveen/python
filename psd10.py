#print prime numbers 

print("Enter the number:")
num=int(input())

flag=0
for i in range(2,num-1):
    if (num % i ==0):
            flag=1
    
if (flag==0):
    print("The number is prime number")
else:
    print("the number is not a prime number")
