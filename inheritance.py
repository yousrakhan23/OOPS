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
