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
    elif position == "w":
        x -= 1
        print(x,y)
    else:
        "Uuuunacceptable!"
    if x==2 and y == 1:        
        print("Victory!")
        switch = True
    