#Blackjack
#Written by Ana Knighten and Ali Purdum
#This program lets you play a simulation of the card game Blackjack


from graphics import *


class Button:
    def __init__(self, name, upperCorner, lowerCorner, textLocation):
        self.name = name
        self.upperCorner = upperCorner
        self.lowerCorner = lowerCorner
        self.textLocation = textLocation
    #draws button boxes
    def drawButton(self, win):
        rectangle = Rectangle(self.upperCorner, self.lowerCorner).draw(win)
        rectangle.setFill("grey")
        Text(self.textLocation, self.name).draw(win)
    #tells which button is clickeed
    def clicked(self, point):
        x = point.getX()
        y = point.getY()
        ucX = self.upperCorner.getX()
        lcX = self.lowerCorner.getX()
        ucY = self.upperCorner.getY()
        lcY = self.lowerCorner.getY()
        if ucX <= x <= lcX and ucY <= y <= lcY:
            return True
        else:
            return False
