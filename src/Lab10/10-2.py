class Animal:
    def __init__(self, type):
        self.type = type

    def sound(self):
        print("No sound")
    
    def display_info(self):
        print("Type: ", self.type)

# Function
class Dog(Animal):

    def __init__(self, type, weight):
        Animal.__init__(self, type)
        self.weight = weight
    
    def sound(self):
        print("Woof")

# Function
class Cat(Animal):

    def __init__(self, type, colour):
        Animal.__init__(self, type)
        self.colour = colour
    
    def sound(self):
        print("Meow")


if __name__ == '__main__':
    my_Dog = Dog("Labrador", 22)
    my_Dog.sound()
    my_Dog.display_info()

    my_cat = Cat("Siamese", "white")
    my_cat.sound()
    my_cat.display_info()
