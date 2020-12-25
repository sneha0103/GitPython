from OopsDemo import Calc
class childImp(Calc):
    num2=200
    def __init__(self):
        Calc.__init__(self, 10,10)
    def getCompleted(self):
        return self.num2+self.num+self.summation()


obj=childImp()
print(obj.getCompleted())

