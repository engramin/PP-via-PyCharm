class Person(object):


    def _init_(self, name, idnumber):   #Constructor
        self.name = name
        self.idnumber = idnumber

    def details(self):
        print("My name is ", self.name)
        print("IdNumber: ", self.idnumber)


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the _init_ of the parent class
        Person._init_(self, name, idnumber)

    def employeedetails(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Salary: {}".format(self.salary))
        print("Post: {}".format(self.post))


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using
# its instance
a.employeedetails()