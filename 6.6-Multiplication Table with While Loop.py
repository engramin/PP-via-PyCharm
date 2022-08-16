number = int(input ("Enter the number of which the user wants to print the multiplication table: "))
count = 1
# we are using while loop for iterating the multiplication 10 times
print ("The Multiplication Table of: ", number)
while count <= 10:
    number = number * 1
    print (number, 'x', i, '=', number * count)
    count += 1