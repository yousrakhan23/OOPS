class Person:
    count = 5 #this is static variable, coz it is defned inside the class, isko hmny constructor may define nhi kra hy.
    
# now make method 

    @staticmethod # this is static method, called predefined decorator.
    def welcome():
        print("Welcome to the class")
        
p1 = Person()

print(p1.welcome()) #count replace to welcome()
print(Person.welcome()) # static variable ko class k through bhi access kr sakty hain, both methods are correct.
