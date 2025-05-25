# an abstract class can be considered a blueprint for other classes, and can't be used to create objects.

from abc import ABC , abstractmethod #abc means abstract

class Human(ABC):
    @abstractmethod
    def __init__(self, name):
        super().__init__()
        self.name = name
        
    @abstractmethod
    def welcome():
        pass # at that time it gives error 
    
class Animal(Human):
    def __init__(self, name, age):
        super().__init__(name) #human ko inherit krdiya , so now ye error ni dega qk human ko we use as template.
        self.age = age
    def welcome(self):
        print("welcome coco")

p1 = Animal("coco", 5)
print(p1.name)
print(p1.age)
print(p1.welcome())