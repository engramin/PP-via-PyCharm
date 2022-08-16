#Class Calculate
#init
#def add
#def divide
#def Multiply
# sef Subtraction

# Create a Class
# Create 4 Methods for Calculation
# Create object of a Class & Pass two values in it
# Perform all the methods by calling through object

# create a class calculator

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def Divide(self):
        return self.num1 / self.num2


print("*******Please select the operation:*********\n" \
      " 1. Add\n " \
      " 2. Subtract\n" \
      " 3. Multiply\n" \
      " 4. Divide\n" \
      )

select = int(input("***Select the operation******\n"))
# (creating the object)

num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
my_Result = Calculator(num1, num2)

if select == 1:
    print(num1, "+", num2, "=", my_Result.add())
elif (select == 2):
    print(num1, "-", num2, "=", my_Result.subtract())
elif (select == 3):
    print(num1, "*", num2, "=", my_Result.multiply())
elif (select == 4):
    print(num1, "/", num2, "=", my_Result.Divide())

else:
    print("invalid number")