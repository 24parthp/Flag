#importing turtle
import turtle
window = turtle.Screen()
window.screensize(canvwidth=1000, canvheight=1000, bg="lightblue")

#var size holds the value that is used to size everything
mainSize = 200
flagLength = mainSize*1.9
stripHeight = mainSize*(1/13)

#colors
colorWhite = "white"
colorRed = "red"
colorNavy = "navy"

#the pointer 
flagPointer = turtle.Turtle()

#changing the turtle speed
flagPointer.speed(0)

#drawing  the flag border
def flagBorder():
    #centering the pointer
    flagPointer.penup()
    flagPointer.goto(0-(flagLength)/2,mainSize/2)

    #drawing the border
    flagPointer.pendown()
    for i in range(2):
        flagPointer.forward(flagLength)
        flagPointer.right(90)
        flagPointer.forward(mainSize)
        flagPointer.right(90)
#drawing the strips
def flagStrips():
    yLocation = mainSize/2
    flagPointer.penup()
    for i in range(13):
        flagPointer.goto(0-(flagLength/2),yLocation-8)
        flagPointer.pendown()
        rem = i % 2
        if(rem == 0):
            flagPointer.color(colorRed)
        else:
            flagPointer.color(colorWhite)
        flagPointer.pensize(stripHeight)
        flagPointer.forward(flagLength)
        flagPointer.penup()
        flagPointer.backward(flagLength)
        yLocation = yLocation - stripHeight
#making a rectangle
def flagStarContainer():
    #positioning the pointer
    flagPointer.goto(0-(flagLength)/2,mainSize/2)
    flagPointer.fillcolor(colorNavy)
    flagPointer.begin_fill()

    #drawing the rectangle
    for i in range(2):
        sqrLength = mainSize*0.76
        sqrWidth = mainSize*(7/13)
        flagPointer.forward(sqrLength)
        flagPointer.right(90)
        flagPointer.forward(sqrWidth)
        flagPointer.right(90)
    flagPointer.end_fill()
#Making stars
def colored_star(x,y):
    #star location info
    starYoffset = mainSize*0.054
    starXLocation = (0-(flagLength/2)+(mainSize*0.063))
    starYLocation = ((mainSize/2))

    #positioing the pointer
    flagPointer.fillcolor(colorWhite)
    flagPointer.begin_fill()
    flagPointer.goto(starXLocation+x, starYLocation-starYoffset+y)
     
    # size of star
    size = mainSize*(0.0616/4)
     
    # object color
    flagPointer.color(colorWhite)
     
    # object width
    flagPointer.width(4)
     
    # angle to form star
    angle = 144
     
    # color to fill
    flagPointer.fillcolor(colorWhite)
    flagPointer.begin_fill()
     
    # form star
    for side in range(5):
        flagPointer.forward(size)
        flagPointer.right(angle)
        flagPointer.forward(size)
        flagPointer.right(72 - angle)
         
    # fill color
    flagPointer.end_fill()

#function that holds calls other functions
def flag():
    flagBorder()
    flagStrips()
    flagStarContainer()
    for i in range(6):
        for k in range(5):
            rem = k % 2
            if(rem == 0):
                colored_star(i*(mainSize*0.063*2)+(mainSize*0.063)+(mainSize*(0.063/2)),k*mainSize*0.054*-1)
            colored_star(i*(mainSize*0.063*2),k*mainSize*0.054*-1)

flag()

window.exitonclick()