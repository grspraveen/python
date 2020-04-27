#user_input1=input("Enter your name:")
#message="hello %s!!" % user_input
#this below script works for python >3.6
#message= f"hello {user_input}"
firstname=input("Enter your first name:")
lastname=input("Enter your last name:")

message1="Hello %s %s" %(firstname, lastname)
message2=f"hello {firstname} {lastname}"
print(message1)
print(message2)
