class Person:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print("Hello")

    def display_info(self):
        print("Name: ", self.name)


class Customer(Person):
    def __init__(self, name, age):
        Person.__init__(self, name)
        self.age = age
    
    def greeting(self):
        print("Dear customers, I am {0} years old".format(self.age))
    
    
if __name__ == '__main__':
    js = Customer('Jone Smith', 20)
    js.greeting()
    js.display_info()
