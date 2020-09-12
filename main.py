import graphics
from graphics import *

def nextbutton():
    clickpos = window.getMouse()
    clickposx = float(str(clickpos)[6:11])
    clickposy = float(str(clickpos)[13:18])
    if (250 < clickposx < 350) and (190 < clickposy < 230):
        return "next"
    else:
        nextbutton()

def parkhrs(hrs):
    if isinstance(hrs, int) == True:
        return True
    else:
        return False
        parkhrs()


window = GraphWin("Phone Bill Calculator", 600, 300)
uin = Image(Point(300, 150), "uin.png")
uentry = Entry(Point(300,170), 60)
uentry.setFill("white")
uot = Image(Point(300, 150), "uot.png")
nextbuttondraw = Text(Point(300, 210), "Calculate")
nextbuttondraw.setSize(20)
nextbuttondraw.setFill("white")
nextbuttonarea = Rectangle(Point(250, 190), Point(350,230))
nextbuttonarea.setFill("red")
output = Text(Point(300,170), "")
output.setSize(25)

uin.draw(window)
uentry.draw(window)
nextbuttonarea.draw(window)
nextbuttondraw.draw(window)
nextbutton()
minutes = uentry.getText()
output.setText("$" + str(27.0 + float(minutes) * 0.53))
nextbuttondraw.undraw()
nextbuttonarea.undraw()
uentry.undraw()
uin.undraw()
uot.draw(window)
output.draw(window)


window.mainloop()