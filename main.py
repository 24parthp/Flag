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
colorLightBlue = 'lightblue'

#the pointer 
flagPointer = turtle.Turtle()

#changing the turtle speed
flagPointer.speed(0)

#drawing  the flag border
def flagBorder():
    #centering the pointer
    flagPointer.penup()
    flagPointer.goto(0-(flagLength)/2,mainSize/2)
    flagPointer.left(90)
    flagPointer.pensize(mainSize*0.025)
    flagPointer.color('black')

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
        flagPointer.goto(0-(flagLength/2),yLocation-(mainSize*0.04))
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
    flagPointer.goto(0-(flagLength)/2,mainSize/2-(mainSize*0.002))
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
    starYoffset = mainSize*0.054/1.25
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
    flagPointer.penup()
#cleaning things up
def cleaning():
    flagPointer.goto(0-(flagLength)/2-(mainSize*.02), mainSize/2+(mainSize*0.05))
    flagPointer.pendown()
    flagPointer.right(90)

    flagPointer.color(colorLightBlue)
    flagPointer.pensize(mainSize*0.05)
    flagPointer.forward(mainSize*1.20)

    flagPointer.penup()
    flagPointer.color(colorLightBlue)
    flagPointer.goto(flagLength/2+(mainSize*.02), mainSize/2+(mainSize*0.05))
    flagPointer.pendown()
    flagPointer.forward(mainSize*1.20)


#function that holds calls other functions
def flag():
    flagStrips()
    flagStarContainer()
    for i in range(11):
        for k in range(5):
            rem = i % 2
            if rem != 0:
                if k == 4:
                    k = 3
                k = k+1/2
                colored_star(i*(mainSize*0.063),k*mainSize*0.054*-1*2)
            colored_star(i*(mainSize*0.063),k*mainSize*0.054*-1*2)
    cleaning()
    flagBorder()
flag()

window.exitonclick()