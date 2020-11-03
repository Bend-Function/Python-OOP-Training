# GitHub repo: https://github.com/Bend-Function/Python-OOP-Training
# DO NOT COPY!
# Author: Bend-Function

from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, name, number_of_wheels):
        self.name = name
        self.number_of_wheels = number_of_wheels

    @abstractmethod
    def display_vehicle(self):
        pass


class Car(Vehicle):

    def __init__(self, name, number_of_wheels, number_of_doors):
        Vehicle.__init__(self, name, number_of_wheels)
        self.number_of_doors = number_of_doors

    def display_vehicle(self):
        print("{0} has {1} wheels and {2} doors".format(self.name, self.number_of_wheels, self.number_of_doors))

# Function
class Bike(Vehicle):

    def __init__(self, name, number_of_wheels, type):
        Vehicle.__init__(self,name, number_of_wheels)
        self.type = type
    
    def display_vehicle(self):
        print("{0} has {1} wheels and is a {2} bike".format(self.name, self.number_of_wheels, self.type))


if __name__ == '__main__':
    v1 = Car("Car", 4, 4)
    v2 = Bike("Bike", 2, "mountain")

    v1.display_vehicle()
    v2.display_vehicle()