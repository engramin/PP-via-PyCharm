#Python defines type conversion functions to directly convert one data type to another ...
#... which is useful in day-to-day and competitive programming.
#There are two types of Type Conversion in Python
#Implicit Type Conversion & Explicit Type Conversion

a=9
b=6
c="Students in Each Batch"

#Implicit Type Conversion
print("a is of type:",type(a))
print("b is of type:",type(b))
c=a+b
print(c)
print ("c of type:",type(c))

#Explicit Type Conversion:
age=input("What is your age?")
print("before coversion:",type(age))
print("After Conversion:",type (int(age)))

