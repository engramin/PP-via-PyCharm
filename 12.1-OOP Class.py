class Car(object):
    def __init__(self, model, passengers, color, speed):
        self.model = model
        self.passengers = passengers
        self.color = color
        self.speed = speed

    def accelerate(self):
        self.speed = self.speed + 2
        print (self.speed)

bmw = Car("BMW", 4, "red", 5)
ferrari = Car("Ferrari", 2, "black", 10)
ford = Car("Ford", 6, "blue", 6)

bmw.accelerate()
print (bmw.color)

ferrari.accelerate()
print (ferrari.color)
ferrari.accelerate() #note that the speed has been updated from the previous accelerate call

print (ford.passengers)
ford.accelerate()