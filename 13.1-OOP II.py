class Million_Coders:   #Class
    batch = "Morning"   #attribute
    def __init__(self, name):    #Constructor
        self.name = name

    def findBatch(self):
            print(self.name, "is in batch of Morning")

            ubaid = Million_Coders("Sajid")   #Object
            waqas = Million_Coders("Waqas")   #Onject

            ubaid.findBatch()
            waqas.findBatch()
