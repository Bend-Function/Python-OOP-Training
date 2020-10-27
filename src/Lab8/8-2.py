class Person:
    name = ""
    age = 0

    def message(self):
        print("Hello")

    def details(self):
        print("My name is {0} and I an {1} years old".format(self.name, self.age))

sam = Person()
sam.name = "Sam"
sam.age = 20

james = Person()
james.name = "James"
james.age = 21

sam.message()
sam.details()
james.message()
james.details()
