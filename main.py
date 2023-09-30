#importing turtle
import turtle
import math
window = turtle.Screen()
window.screensize(canvwidth=1000, canvheight=1000, bg="lightblue")

#var size holds the value that is used to size everything
mainSize = 200
flagLength = mainSize*1.9
stripeHeight = mainSize*(1/13)

#colors
backgroundColor = "lightblue"

#assigning the pointer 
flagPointer = turtle.Turtle()

#changing the turtle speed
flagPointer.speed(7)

#Basic functions
#drawing  the flag border
def flagBorder():
    #centering the pointer
    flagPointer.penup()
    flagPointer.goto(0-(flagLength)/2,mainSize/2)
    flagPointer.seth(0)
    flagPointer.pensize(mainSize*0.025)
    flagPointer.color('black')

    #drawing the border
    flagPointer.pendown()
    for i in range(2):
        flagPointer.forward(flagLength)
        flagPointer.right(90)
        flagPointer.forward(mainSize)
        flagPointer.right(90)
    flagPointer.penup()
#cleaning up the side of flag
def cleaning():
    flagPointer.penup()
    flagPointer.goto(0-(flagLength)/2-(mainSize*.25), mainSize/2+(mainSize*0.25))
    flagPointer.seth(0)
    flagPointer.pensize(mainSize*0.50)
    flagPointer.pencolor(backgroundColor)

    flagPointer.pendown()

    for i in range(2):
        flagPointer.forward(flagLength*1.27)
        flagPointer.right(90)
        flagPointer.forward(mainSize*1.50)
        flagPointer.right(90)
#Erasing the previous flag
def eraseFlag():
    eraseSize = mainSize/4+(mainSize*0.05)
    pointerYoffset = eraseSize/2-(mainSize*0.015)
    #reset the point to top left of flag
    flagPointer.penup()
    flagPointer.goto(0-(flagLength)/2,mainSize/2-pointerYoffset)
    flagPointer.seth(0)

    #painter over the flag
    flagPointer.pendown()
    flagPointer.color(backgroundColor)
    flagPointer.pensize(eraseSize)
    for i in range(4):
        flagPointer.goto(0-(flagLength)/2,mainSize/2-pointerYoffset)
        flagPointer.forward(flagLength)
        pointerYoffset = pointerYoffset + eraseSize
    flagPointer.penup()

#Cleaning -> Border -> erasing 
def afterFlag():
    cleaning()
    flagBorder()
    eraseFlag()


#Draws the US flag
def USFlag():

    #US flag color
    USflagWhite = "#FFFFFF"
    USflagRed = "#B31942"
    USflagBlue = '#0A3161'

    #drawing the stripes
    def usFlagstripes( ):
        yLocation = mainSize/2
        flagPointer.penup()
        for i in range(13):
            flagPointer.goto(0-(flagLength/2),yLocation-(mainSize*0.04))
            flagPointer.pendown()
            rem = i % 2
            if(rem == 0):
                flagPointer.pencolor(USflagRed)
            else:
                flagPointer.pencolor(USflagWhite)
            flagPointer.pensize(stripeHeight)
            flagPointer.forward(flagLength)
            flagPointer.penup()
            flagPointer.backward(flagLength)
            yLocation = yLocation - stripeHeight
    #making a rectangle
    def usFlagStarContainer():
        #positioning the pointer
        flagPointer.goto(0-(flagLength)/2,mainSize/2-(mainSize*0.002))
        flagPointer.fillcolor(backgroundColor)
        flagPointer.begin_fill()

        #drawing the rectangle
        flagPointer.color(USflagBlue)
        for i in range(2):
            sqrLength = mainSize*0.76
            sqrWidth = mainSize*(7/13)
            flagPointer.forward(sqrLength)
            flagPointer.right(90)
            flagPointer.forward(sqrWidth)
            flagPointer.right(90)
        flagPointer.end_fill()
    #Making stars
    def usColored_star(x,y):
        #star location info
        starYoffset = mainSize*0.054/1.25
        starXLocation = (0-(flagLength/2)+(mainSize*0.063))
        starYLocation = ((mainSize/2))

        #positioing the pointer
        flagPointer.fillcolor(USflagWhite)
        flagPointer.begin_fill()
        flagPointer.goto(starXLocation+x, starYLocation-starYoffset+y)
        
        # size of star
        size = mainSize*(0.0616/4)
        
        # object color
        flagPointer.pencolor(USflagWhite)
        
        # object width
        flagPointer.width(4)
        
        # angle to form star
        angle = 144
        
        # color to fill
        flagPointer.fillcolor(USflagWhite)
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

    #calling the functions
    usFlagstripes()
    usFlagStarContainer()
    """for i in range(11):
        for k in range(5):
            rem = i % 2
            if rem != 0:
                if k == 4:
                    k = 3
                k = k+1/2
                usColored_star(i*(mainSize*0.063),k*mainSize*0.054*-1*2)
            usColored_star(i*(mainSize*0.063),k*mainSize*0.054*-1*2)
    """
    afterFlag()
#Draws the Chad flag
def chadFlag():

    def chadFlagStripes():
        Yadd = flagLength/3/2
        stripeSize = flagLength/3

        flagPointer.penup()
        flagPointer.pensize(stripeSize)
        flagPointer.seth(0)

        for i in range(3):
            flagPointer.goto(0-(flagLength)/2+Yadd,mainSize/2)
            flagPointer.right(90)
            if i == 0:
                flagPointer.color("#002664")
            elif i == 1:
                flagPointer.color("#fecb00")
            elif i == 2:
                flagPointer.color("#c60c30")
            flagPointer.pendown()
            flagPointer.forward(mainSize*1)
            flagPointer.right(270)
            flagPointer.penup()
            Yadd = Yadd + flagLength/3

    #calling the functions
    chadFlagStripes()
    afterFlag()
#Draws the Luxembourg flag
def luxembourgFlag():

    def luxembourgStripes():
        Yoffset = mainSize/3/2

        flagPointer.penup()
        flagPointer.goto(0-(flagLength)/2,mainSize/2-Yoffset)
        flagPointer.pensize(mainSize/3)
        flagPointer.seth(0)

        for i in range(3):
            flagPointer.pendown()
            if i == 0:
                flagPointer.color('#EF3340')
            elif i == 1:
                flagPointer.color("#FFFFFF")
            elif i == 2:
                flagPointer.color("#00A3E0")
            flagPointer.fd(flagLength)
            flagPointer.penup()
            Yoffset = Yoffset + mainSize/3
            flagPointer.goto(0-(flagLength)/2,mainSize/2-Yoffset)

    #calling the functions
    luxembourgStripes()
    afterFlag()
#Draws the Columbian flag
def columbiaFlag():

    def columbiaStripes():
        Yoffset = mainSize/4/2

        flagPointer.penup()
        flagPointer.goto(0-(flagLength)/2,mainSize/2-Yoffset)
        flagPointer.pensize(mainSize/4)
        flagPointer.seth(0)

        for i in range(4):
            flagPointer.pendown()
            if i == 0 or i == 1:
                flagPointer.color('#FCD116')
            elif i == 2:
                flagPointer.color("#003893")
            elif i == 3:
                flagPointer.color("#CE1126")
            flagPointer.fd(flagLength)
            flagPointer.penup()
            Yoffset = Yoffset + mainSize/4
            flagPointer.goto(0-(flagLength)/2,mainSize/2-Yoffset)

    #calling the functions
    columbiaStripes()
    afterFlag()
#Draws the Iceland flag
def iceLandFlag():

    #Blue background
    def icelandBackground():

        flagPointer.penup()
        flagPointer.goto(0-(flagLength)/2,mainSize/2)
        flagPointer.seth(0)

        flagPointer.fillcolor('#02529C')
        flagPointer.begin_fill()
        for i in range(2):
            flagPointer.fd(flagLength)
            flagPointer.right(90)
            flagPointer.fd(mainSize)
            flagPointer.right(90)

        flagPointer.end_fill()
    #White perpendicular stripes
    def icelandWhiteStripes():
        flagPointer.color('#FFFFFF')
        flagPointer.goto(0-flagLength/2-(flagLength*0.01), 0)
        flagPointer.seth(0)
        flagPointer.pensize(mainSize*(4/18))
        flagPointer.pendown()
        flagPointer.fd(flagLength*1.01)
        flagPointer.penup()

        flagPointer.goto(0-flagLength/2+(flagLength*(4/12.5)),mainSize/2)
        flagPointer.right(90)
        flagPointer.pendown()
        flagPointer.fd(mainSize)
        flagPointer.penup()
    #Red Perpendicular stripes
    def icelandRedStripes():
        flagPointer.color('#DC1E35')
        flagPointer.goto(0-flagLength/2-(flagLength*0.01), 0)
        flagPointer.seth(0)
        flagPointer.pensize(mainSize*(2/18))
        flagPointer.pendown()
        flagPointer.fd(flagLength*1.01)
        flagPointer.penup()

        flagPointer.goto(0-flagLength/2+(flagLength*(4/12.5)),mainSize/2)
        flagPointer.right(90)
        flagPointer.pendown()
        flagPointer.fd(mainSize)
        flagPointer.penup()

    #calling the functions
    icelandBackground()
    icelandWhiteStripes()
    icelandRedStripes()
    afterFlag()
#Draws the Jamaica Flag
def jamaicaFlag():
    #green background
    def jamaicaBackground():


        flagPointer.penup()
        flagPointer.goto(0-(flagLength)/2,mainSize/2)
        flagPointer.seth(0)

        flagPointer.fillcolor('#009B3A')
        flagPointer.begin_fill()
        for i in range(2):
            flagPointer.fd(flagLength)
            flagPointer.right(90)
            flagPointer.fd(mainSize)
            flagPointer.right(90)

        flagPointer.end_fill()
    #black triangle
    def jamaicaBlackTri():
        flagPointer.penup()
        flagPointer.goto(0-(flagLength)/2,mainSize/2)
        flagPointer.fillcolor("black")
        flagPointer.color('black')
        flagPointer.pensize(mainSize*0.01)

        #Drawing and filling the left triangle
        flagPointer.pendown()
        flagPointer.begin_fill()
        flagPointer.seth(math.degrees(math.atan((-mainSize/2)/(flagLength/2))))
        flagPointer.fd(math.sqrt((mainSize/2)**2+(flagLength/2)**2))

        flagPointer.seth(math.degrees(math.atan((mainSize/2)/(flagLength/2))))
        flagPointer.fd(math.sqrt((mainSize/2)**2+(flagLength/2)**2)*-1)

        flagPointer.seth(90)
        flagPointer.fd(mainSize)

        flagPointer.end_fill()
        flagPointer.penup()

        #Drawing and filling the right triangle
        flagPointer.goto(0+(flagLength)/2,mainSize/2)
        flagPointer.pendown()
        flagPointer.begin_fill()
        flagPointer.seth(math.degrees(math.atan((mainSize/2)/(flagLength/2))))
        flagPointer.fd(math.sqrt((mainSize/2)**2+(flagLength/2)**2)*-1)

        flagPointer.seth(math.degrees(math.atan((-mainSize/2)/(flagLength/2))))
        flagPointer.fd(math.sqrt((mainSize/2)**2+(flagLength/2)**2))

        flagPointer.seth(90)
        flagPointer.fd(mainSize)

        flagPointer.end_fill()
    #yellow stripes
    def jamaicaYellowStrips():
        flagPointer.penup()
        flagPointer.goto(0-(flagLength)/2,mainSize/2)
        flagPointer.pensize(mainSize*0.2)
        flagPointer.color("#FED100")

        flagPointer.pendown()
        flagPointer.seth(math.degrees(math.atan(-mainSize/flagLength)))
        flagPointer.fd(math.sqrt(mainSize**2+flagLength**2))

        flagPointer.penup()
        flagPointer.goto(0+(flagLength)/2,mainSize/2)

        flagPointer.pendown()
        flagPointer.seth(math.degrees(math.atan(mainSize/flagLength)))
        flagPointer.fd(math.sqrt(mainSize**2+flagLength**2)*-1)

    #calling the functions
    jamaicaBackground()
    jamaicaBlackTri()
    jamaicaYellowStrips()
    afterFlag()


#Draws every flag
def flag():
    USFlag()
    chadFlag()
    luxembourgFlag()
    columbiaFlag()
    iceLandFlag()
    jamaicaFlag()

flag()

window.exitonclick()