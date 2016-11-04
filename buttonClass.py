#COM 110 Graphical User Interfaces (GUIs)
#button.py program
#
#This program creates a button
#Has a method to draw the button and check whether a point is in the button.
#

from graphics import *


class Button():

         #constructor for a button- needs graphics window, position, color,h,w,string
            #assumes a setCoords has taken place
    def __init__(self,win, x,y,height,width,color, textColor,label=''):
        self.window=win
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.color=color
        self.textColor=textColor
        self.label=label

            #draw the button- the label will be white
    def draw(self):
        self.rec=Rectangle(Point(self.x-self.width/2,self.y-self.height/2), Point(self.x+self.width/2,self.y+self.height/2))
        self.rec.setFill(self.color)
        self.rec.draw(self.window)
            #Put label on button
        self.recLabel = Text(Point(self.x,self.y),self.label)
        self.recLabel.setFill(self.textColor)
        self.recLabel.draw(self.window)

    def undraw(self):
        self.rec.undraw()
        self.recLabel.undraw()
        
            #see if pt is in the button
    def clicked(self, pt):
        if pt.getX()>=self.x-self.width/2.0 and pt.getX()<=self.x+self.width/2.0 and pt.getY()>=self.y-self.height/2.0 and pt.getY()<=self.y+self.height/2.0:
            return True
        else:
            return False

    def setColor(self, color):
        self.rec.setFill(color)

    def setOutline(self, color):
        self.rec.setOutline(color)

    def setTextColor(self, color):
        self.recLabel.setFill(color)

    def getLabelText(self):
        return self.label

    def setLabelText(self, label):
        self.label = label

    def getCoords(self):
        return self.x, self.y
