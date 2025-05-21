# 1st class

class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def welcome(self):
        print(f"welcome {self.name}")
        
# 2nd class

class Student(Person):
    def __init__ (self, name, age, gmail, rollno):
        super(). __init__(name, age) # you can also write Person() instead of super()
        self.gmail = gmail
        self.rollno = rollno

p1 = Student("Yousra Khan", 45, "yousrakhanzaigmail.com", 267488)
print("name:", p1.name)
print("age:", p1.age)
print("mail:", p1.gmail)
print("roll number:", p1.rollno)
p1.welcome()


# multiple class 

class Person:
    def __init__ (self, name):
        self.name = name
    def welcome(self):
        print(f"welcome Person")
        
class Game:
    def __init__ (self, game):
        self.game = game
    def welcome(self):
        print(f"welcome Person")  
        
class Player(Person, Game):
    def __init__ (self,name,game,age):
        Person.__init__(self,name)
        Game.__init__(self,game)
        self.age = age
        
p1 = Player("Imran Khan", "Cricket", 45)
print("name:", p1.name)
print("game:", p1.game)
print("age:", p1.age)
p1.welcome() # this will call the welcome method of the Person class, coz it is the first class in the inheritance, sequence matter.