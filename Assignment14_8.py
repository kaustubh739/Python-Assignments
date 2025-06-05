# create a class vehicle with method start(). derive class car and override the method start() with additional behaviour. show method overriding.
class Vehicle:

    def start(self):
        print("In a parent class")

class Car(Vehicle):

    def start(self):
        print("In a child class")

obj = Car()
obj.start()

obj = Vehicle()
obj.start()