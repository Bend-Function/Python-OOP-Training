class Person:
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        print("Getting the age")
        return self.__age

    @age.setter
    def age(self, value):
        print("Setting the age")
        if value < 0 or value > 100:
            print("Age value must be less than 100 and greater than 0.")
            self.__age = 0
        else:
            self.__age = value

    def __message(self):
        print("Hello")

    def details(self):
        print("My name is {0} and I an {1} years old".format(self.__name, self.__age))

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, value):
        if(value):
            self.__name = value
        else:
            print("Name value must be str not none.")
            
if __name__ == '__main__':
    sam = Person("Sam", 20)
    james = Person("James", 21)

    sam.age = 30
    print(sam.age)

