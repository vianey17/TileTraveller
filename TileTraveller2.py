""" def tiletraveller(i):
    switch = True
    
    if i=="y":
        print("Switch is true!")
        return switch
    else:
        print("Switch is false!")
        return i
switch = False
i = "h"
print(tiletraveller(i)) """


""" 
You can travel: (N)orth.
Direction: s
Not a valid direction!
Direction: n
Victory! 
"""
def TileTraveller(x,y,position):
    

    print("You can travel:, ")
    switch = True
    return switch
x = 1
y = 1
switch = False
position = str(input("Input your direction:"))
while switch == False:
    TileTraveller(x,y,position)