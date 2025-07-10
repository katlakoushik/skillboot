class Cat:
    def make_sound(self):
        pass
class Dog(Cat):
    def make_sound(self):
        print("Dog sound")
class Cat2(Cat):
    def make_sound(self):
        print("Cat sound")
for v in [Dog(), Cat2()]:
    v.make_sound()