class Computer: 

    def __init__(self, company):
        self.__company = company

    def __private_say_company(self):
        print("The company is called %s"%self.__company)
    
    def public_say_company(self):
        self.__private_say_company()

class Phone:
    def __init__(self, phone_number):
        self.__phone_number = phone_number

    def get_phone_number(self):
        return self.__phone_number


class Smartphone(Computer, Phone):

    def __init__(self, company, phone_number, name):
        Computer.__init__(self, company)
        Phone.__init__(self, phone_number)
        self.__name = name

    def get_name(self):
        return self.__name
    

sp1 = Smartphone("Apple", 15257918341, "iPhone X")
sp1.public_say_company()
print(sp1.get_phone_number())
print(sp1.get_name())

