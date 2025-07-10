class Account:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__balance=0
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getBalance(self):
        return self.__balance
    def setBalance(self,balance):
        self.__balance += balance
acc=Account(name="john",age=22)
print(acc.getName())
print(acc.getBalance())
acc.setBalance(99)
print(acc.getBalance())
