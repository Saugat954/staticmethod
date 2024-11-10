
class Number:
    def __init__(self,num):
        self.num = num

    def addtoNum(self,n):
        self.num = self.num + n
    #we are not required to use self in the static method
    @staticmethod
    def add(a,b):
        return a+b
    
a=Number(5)
print(a.num)
a.addtoNum(3)
print(a.num)



result = Number.add(2, 3)  # Using the static method to add two numbers
print(result)  