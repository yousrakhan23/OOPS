# make a class

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def welcome(self):
        print(f"WELCOME {self.name}")
p1 = Person("Yousra Khan", 46)
p2 = Person("Hassan Khan", 47)
print("name:", p1.name )
print("age:", p1.age)
print("name:", p2.name)
print("age:", p2.age)
print(p1.name, "is happily married to", p2.name)
p1.welcome()


