def adult_finder(age):
    if (age > 18):
        return "major"
    else:
        return "minor"

print ("Please enter the age:")
age=float(input())
print(adult_finder(age))

