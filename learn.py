"""
automobile_euro=set(["audi","BMW","merc","skoda"])
automobile_india=set(["hyundai","maruthi","toyoto","skoda"])
all_brands=automobile_euro & automobile_india
print(all_brands)

word ="This is Python"
know='P' in word
print(know)


test_score1=(12,23,34)
test_score2=(45,55,67)
test=test_score1+ test_score2
print(test)
type(test)


age=(12,23,34) *3 
print(age)

age=[12,23,34] *3 
print(age)
"""

"""
def my_function(arg1, arg2):
    changed_name=("my first name %s last name  %s" %(arg1,arg2))
    return changed_name

print(my_function("myra", "gummadidala"))
print(my_function("praveen", "GRS"))
print(my_function("chandrika", "nippani"))
"""

def multi_return(): 
    age=30
    name="praveen"
    address="lingampally "
    return age, name, address

age,name,address=multi_return()
print(age,name,address)






