# it means only hiding complex details and showing only the imporatant fetures

from abc import ABC , abstractmethod

class vehicle(ABC):
    
    @abstractmethod
    def start(self):
        pass

    #child class
class Car(vehicle):
        def start(self):
            print("Car starts with key")
            
class Bike(vehicle):
        def start(self):
            print("bike starts with button")
            
#objection creation

c = Car()
c.start()

b = Bike()
b.start()