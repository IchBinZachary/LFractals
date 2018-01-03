#Zachary Zysberg 110801274
#CSE 101
#Prof. Tashbook
from turtle import *

pattern = ''

meme = Turtle()
memescreen=meme.getscreen()
distance = int(memescreen.numinput("Distance","Type in the value for 'distance'.", 10, 5,25))
angle = int(memescreen.numinput("Angle","Type in the value for angle of rotation.", 90, 1, 360))
seed = str(memescreen.textinput("Seed","Type in the pattern to draw out."))
depth = int(memescreen.numinput("Depth","Type in the value for depth of the pattern.", 6, 1, 12))


#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#               X   --> X--YF                    For every occurence of X, replace with X-YF
#               Y   -->FX+Y                     For every occurence of Y, replace with FX+Y
#||||||||||||||Production Rule Set|||||||||||||||||||||Also Called Productions (Reference to parameter in deriveLSystem)|||||||||||||||||||||||||||||||||||||||||||||||||||||||||


ecksandwhy = {'X':'X-YF','Y':'FX+Y'}


def deriveLSystem(seed,productions,depth): #Seed is the starting string
    global pattern
                                                                         #Productions is a dictionary where the keys are characters to replace
    for i in range(depth):
        temp = ''                                                                    #Depth is the current recursion depth
        for o in seed:                                                  #||||||Purpose of this is to derive the final string to draw|||||
            if o in productions.keys():
                temp = temp + productions[o]
            else:
                temp=temp+o
        seed = temp        
    return seed
            
            
                                                                   
def drawLSystem(string, angle, distance):
    meme.pendown()
    meme.speed(0)
    for item in string:
        if item == 'F':
            meme.forward(distance)
        elif item == '+':
            meme.right(angle)
        elif item == '-':
            meme.left(angle)                    
        
            
string = deriveLSystem(seed,ecksandwhy,depth)
print(string)
drawLSystem(string, angle, distance)
