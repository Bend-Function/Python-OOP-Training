class Person:
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __message(self):
        print("Hello")

    def details(self):
        print("My name is {0} and I an {1} years old".format(self.__name, self.__age))

    def get_name(self):
        return self.__name

    def set_name(self, value):
        if(value):
            self.__name = value
        else:
            print("Name value must be str not none.")
            
    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 0 or value > 100:
            print("Age value must be less than 100 and greater than 0.")
        else:
            self.__age = value

    age = property(get_age, set_age)

if __name__ == '__main__':
    sam = Person("Sam", 20)
    james = Person("James", 21)

    sam.age = 130
    print(sam.age)

