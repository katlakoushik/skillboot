class Vehicle:
    def navigate(self):
        pass
class Car(Vehicle):
    def navigate(self):
        print("navigate through vehicle")
class Engine(Vehicle):
    def navigate(self):
        print("navigate through engine")
for v in [Car(), Engine()]:
    v.navigate()