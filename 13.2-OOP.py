class Million_Coders:  # class

    batch = "Morning"  # attribute

    def __init__(self, name):  # constructor
        self.name = name

    def findBatch(self):
        print(self.name, "is in batch of Morning")


ubaid = Million_Coders("Sajid")  # object
waqas = Million_Coders("Waqas")  # object


ubaid.findBatch()
waqas.findBatch()

# print("Ubaid is batch of", ubaid.batch)  # calling class attribute using its object