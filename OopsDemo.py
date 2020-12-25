# self keyword is manadatory to call methods
# New keyword is not used to create object
# class and instance variable has different purpose
# __init__ is the name of constructor
class Calc:
    num = 100 #class variable
    def __init__(self, a, b):
        self.firstnum = a
        # instance Variable
        self.secondnum = b
        print("Constructor Calling")
    def getData(self):
     print("executing as method in class")
    def summation(self):
        return self.firstnum+self.secondnum+Calc.num


obj=Calc(5,4) #creating Objects
obj.getData()
print(obj.summation())

obj1=Calc(50,40) #creating Objects
obj1.getData()
print(obj1.summation())