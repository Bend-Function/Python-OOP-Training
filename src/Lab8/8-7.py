class Person:
    
    number_of_people = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
        Person.number_of_people += 1
        print("Added 1 person")


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0 or value > 100:
            print("Age value must be less than 100 and greater than 0.")
            self.__age = 0
        else:
            self.__age = value

    @staticmethod
    def message():
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

    @classmethod
    def count_population(cls):
        print("There are {0} people".format(Person.number_of_people))

            
if __name__ == '__main__':
    Person.message()
    tim = Person("Tim", 29)
    Person.count_population()
    alice = Person("Alice", 25)
    Person.count_population()

