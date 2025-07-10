from abc import ABC, abstractmethod
class Dog(ABC):
    @abstractmethod
    def make_sound(self):
        print("Dog sound")
class Cat(Dog):
    def make_sound(self):
        print("Cat sound")
obj = Cat()
obj.make_sound()