#Blackjack
#Written by Ana Knighten and Ali Purdum
#This program lets you play a simulation of the card game Blackjack




from graphics import *


class Player:
    def __init__(self, hand, Deck, score = 0, money = 100):
        self.hand = hand
        self.money = money
        self.score = score

    #creates player hand
    def newHand(self, Deck):
        hand = Deck.createHand()
        self.hand = hand

    #subtracts bet money if you lose round
    def loseBet(self, betmoney):
        self.money = self.money - betmoney
        return self.money

    #adds bet amount*2 if you win round
    def winBet(self, betmoney):
        self.money = self.money + betmoney*2
        return self.money

    #adds card to hand
    def hit(self, Deck):
        card = Deck.deal()
        self.hand.append(card)

    #keeps track of card total
    def addScore(self, hand):
        self.score = 0
        for card in hand:
            self.score = self.score + int(card[1])
        return self.score
    #draws cards to graphics window
    def drawCard(self, win):
        x = 80
        y = 400
        imageList = []
        for card in self.hand:
            cardImage = card[2]
            drawImage = Image(Point(x, y), cardImage).draw(win)
            x = x + 40
            imageList.append(drawImage)
        return imageList
    #undraws cards from graphics window
    def undrawCard(self, win, imageList):
        for drawImage in imageList:
            drawImage.undraw()
    #draws total of cards in hand
    def drawScore(self, win):
        drawscore = Text(Point(370, 400), "You have a total of " + str(self.score) + "!").draw(win)
        drawscore.setSize(14)
        return drawscore
