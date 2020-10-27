class Person:
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __message(self):
        print("Hello")

    def details(self):
        print("My name is {0} and I an {1} years old".format(self.__name, self.__age))

sam = Person("Sam", 20)
james = Person("James", 21)

print(sam._Person__name)
