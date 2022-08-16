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

class Calculate:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def addition(self):
        print("The Addition of ", self.val1, " and ", self.val2, "is ", self.val1+self.val2)

    def subtraction(self):
        print("The Subtraction of ", self.val1, " and ", self.val2, "is ", self.val1-self.val2)

    def multiplication(self):
        print("The Multiplication of ", self.val1, " and ", self.val2, "is ", self.val1*self.val2)

    def division(self):
        print("The Divsion of ", self.val1, " and ", self.val2, "is ", self.val1/self.val2)


cal = Calculate(30,40)

cal.addition()
cal.subtraction()
cal.division()
cal.multiplication()