""" 
You can travel: (N)orth.
Direction: s
Not a valid direction!
Direction: n
Victory! 
"""

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
            y += 1
            print(x,y)
        else:
            print("Not a valid direction!")
    
    elif (x==1 and y==2):
        print("You can travel: (N)orth, (S)outh, or (E)ast")
        position = str(input("Direction:"))
        if position == "n":
            y += 1
            print(x,y)
        elif position == "e":
            x += 1
            print(x,y)
        elif position == "s":
            y -= 1
            print(x,y)
        else:
            print("Not a valid direction!")
    
    elif (x==1 and y == 3):
        print("You can travel: (S)outh or (E)ast")
        position = str(input("Direction:"))
        
        if position == "e":
            x += 1
            print(x,y)
        elif position == "s":
            y -= 1
            print(x,y)
        else:
            print("Not a valid direction!")
    
    elif (x==2 and y == 3):
        print("You can travel: (E)ast or (W)est")
        position = str(input("Direction:"))
        
        if position == "e":
            x += 1
            print(x,y)
        elif position == "w":
            x -= 1
            print(x,y)
        else:
            print("Not a valid direction!")
    
    elif (x==2 and y==2) or (x == 3 and y ==3):
        print("You can travel: (S)outh or (W)est")
        position = str(input("Direction:"))

        if position == "s":
            y -= 1
            print(x,y)
        elif position == "w":
            x -= 1
            print(x,y)
        else:
            print("Not a valid direction!")
    elif (x==3 and y==2):
        print("You can travel: (N)orth or (S)outh")
        position = str(input("Direction:"))

        if position == "s":
            y -= 1
            print(x,y)
        elif position == "n":
            y += 1
            print(x,y)
        else:
            print("Not a valid direction!")

    if x==3 and y == 1:        
        print("Victory!")
        switch = True
    