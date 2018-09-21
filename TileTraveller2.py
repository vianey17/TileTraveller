""" 
1. The first implementation was easier because it required more basic thinking and it wasn't adapting any other code. 
2. The second one seems more readable because it contains less lines.
3. I was mostly looking to stop the endless repetition of code.
"""
def reposition(x,y,position):
    if position == "n":
            y += 1
            return y
            
    elif position == "e":
            x += 1
            return x
            
    elif position == "s":
            y -= 1
            return y
    elif position == "w":
            x -= 1
            return x
def invalid():
    print("Not a valid direction!")

           
#Initial position
x = 1
y = 1

position = 0

switch = False

while switch==False:
    
    if (x==1 and y ==1) or (x==2 and y ==1):
        print("You can travel: (N)orth")
        position = str(input("Direction:"))
        if position == "n":
            reposition(x,y,position)
        else:
            invalid()
    
    elif (x==1 and y==2):
        print("You can travel: (N)orth, (S)outh, or (E)ast")
        position = str(input("Direction:"))
        if position == "n" or position =="e" or position == "s":
            reposition(x,y,position)
        else:
            invalid()
    
    elif (x==1 and y == 3):
        print("You can travel: (S)outh or (E)ast")
        position = str(input("Direction:"))
        
        if position == "e" or position == "s":
            reposition(x,y,position)
        else:
            invalid()
    
    elif (x==2 and y == 3):
        print("You can travel: (E)ast or (W)est")
        position = str(input("Direction:"))
        
        if position == "e" or position == "w":
            reposition(x,y,position)
        else:
            invalid()
    
    elif (x==2 and y==2) or (x == 3 and y ==3):
        print("You can travel: (S)outh or (W)est")
        position = str(input("Direction:"))

        if position == "s" or position == "w":
           reposition(x,y,position)
        else:
            invalid()
    elif (x==3 and y==2):
        print("You can travel: (N)orth or (S)outh")
        position = str(input("Direction:"))

        if position == "s" or position == "n":
            reposition(x,y,position)
        else:
            invalid()

    if x==3 and y == 1:        
        print("Victory!")
        switch = True
    