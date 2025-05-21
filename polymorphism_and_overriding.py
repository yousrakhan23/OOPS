# overriding

class Cricket:
    def play(self,game):
        print(f"players are playing {game}")

# now make another class

class Football(Cricket):
    # pass # remove pass and copy the function from Cricket class
    def play(self,game):
        print(f"players are playing {game}.......") # here priority is given to this function, jo inherit hua tha function wo nhi chala
        
p1 = Cricket() 
p2 = Football()

p1.play("Cricket")
p2.play("Football")

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# polymorphism

class Cricket:
    def play(self,game):
        print(f"players are playing {game}")

# now make another class

class Football(Cricket):
    # pass # remove pass and copy the function from Cricket class
    def play(self,game):
        print(f"players are playing {game}.......") # here priority is given to this function, jo inherit hua tha function wo nhi chala
        

p2: Cricket = Football() # cricket , type hy football kii and football is instance, polymorphism run time pr decide krta hy k konsa function call krna hy,
# run time pr cricket wali type may jo method hy usko call nhi krna , iska jo instance y (football) isky method ko call krna, qk in dono k name same hy, 
# same function call ho rha hy , 


p2.play("Football")