class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price
s1=Product(name="john",age=22)
print(s1.getName())
print(s1.getPrice())