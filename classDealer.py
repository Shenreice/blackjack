#Blackjack
#Written by Ana Knighten and Ali Purdum
#This program lets you play a simulation of the card game Blackjack



from graphics import *

class Dealer:
    def __init__(self, hand, Deck, score = 0):
        self.hand = hand
        self.score = score

    #creates dealer hand
    def newHand(self, Deck):
        hand = Deck.createHand()
        self.hand = hand

    #adds card to hand
    def hit(self, Deck):
        card = Deck.deal()
        self.hand.append(card)

    #keeps track of score
    def addScore(self, hand):
        self.score = 0
        for card in hand:
            self.score = self.score + int(card[1])
        return self.score

    #draws first card to graphic window
    def drawCard(self, win):
        x = 80
        y = 180
        imageList = []
        for card in self.hand:
            cardImage = card[2]
        drawImage = Image(Point(x, y), cardImage).draw(win)
        imageList.append(drawImage)
        return imageList

    #draws remaining cards to graphic window
    def drawAllCard(self, win):
        x = 80
        y = 180
        imageList = []
        for card in self.hand:
            cardImage = card[2]
            drawImage = Image(Point(x, y), cardImage).draw(win)
            x = x + 40
            imageList.append(drawImage)
        return imageList
    #undraws cards
    def undrawCard(self, win, imageList):
        for drawImage in imageList:
            drawImage.undraw()
    #draws dealer cards total
    def drawScore(self, win):
        drawscore = Text(Point(370, 200), "The dealer has a total of " + str(self.score) + "!").draw(win)
        drawscore.setSize(14)
        return drawscore
