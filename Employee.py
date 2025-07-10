class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.price=100
    def getName(self):
        print(self.name)
class Manager(Employee):
    def method(self):
        print(self.name,self.age,self.price)

b=Manager(name="john",age=22)
b.method()
b.getName()
