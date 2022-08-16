# Multiplication table (from 1 to 10) in Python

num = 5

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
   print('---')

number = int(input ("Enter the number of which the user wants to print the multiplication table: "))
count = 1
# we are using while loop for iterating the multiplication 10 times
print ("The Multiplication Table of: ", number)
while count <= 10:
    number = number * 1
    print (number, 'x', i, '=', number * count)
    count += 1