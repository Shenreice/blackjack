#Blackjack
#Written by Ana Knighten and Ali Purdum
#This program lets you play a simulation of the card game Blackjack

import random

class Deck:
    #creates deck of cards
    def __init__(self):
        self.Deck = [("Ace of Hearts", 11, "AH.png"), ("2 of Hearts", 2, "2H.png"), \
        ("3 of Hearts", 3, "3H.png"), ("4 of Hearts", 4, "4H.png"), \
        ("5 of Hearts", 5, "5H.png"), ("6 of Hearts", 6, "6H.png"), \
        ("7 of Hearts", 7, "7H.png"), ("8 of Hearts", 8, "8H.png"), \
        ("9 of Hearts", 9, "9H.png"), ("10 of Hearts", 10, "10H.png"), \
        ("Jack of Hearts", 10, "JH.png"), ("Queen of Hearts", 10, "QH.png"), \
        ("King of Hearts", 10, "KH.png"), ("Ace of Spades", 11, "AS.png"), \
        ("2 of Spades", 2, "2S.png"), ("3 of Spades", 3, "3S.png"), \
        ("4 of Spades", 4, "4S.png"), ("5 of Spades", 5, "5S.png"), \
        ("6 of Spades", 6, "6S.png"), ("7 of Spades", 7, "7S.png"), \
        ("8 of Spades", 8, "8S.png"), ("9 of Spades", 9, "9S.png"), \
        ("10 of Spades", 10, "10S.png"), ("Jack of Spades", 10, "JS.png"), \
        ("Queen of Spades", 10, "QS.png"), ("King of Spades", 10, "KS.png"), \
        ("Ace of Diamonds", 11, "AD.png"), ("2 of Diamonds", 2, "2D.png"), \
        ("3 of Diamonds", 3, "3D.png"), ("4 of Diamonds", 4, "4D.png"), \
        ("5 of Diamonds", 5, "5D.png"), ("6 of Diamonds", 6, "6D.png"), \
        ("7 of Diamonds", 7, "7D.png"), ("8 of Diamonds", 8, "8D.png"), \
        ("9 of Diamonds", 9, "9D.png"), ("10 of Diamonds", 10, "10D.png"), \
        ("Jack of Diamonds", 10, "10D.png"), ("Queen of Diamonds", 10, "QD.png"), \
        ("King of Diamonds", 10, "KD.png"), ("Ace of Clubs", 11, "AC.png"), \
        ("2 of Clubs", 2, "2C.png"), ("3 of Clubs", 3, "3C.png"), \
        ("4 of Clubs", 4, "4C.png"), ("5 of Clubs", 5, "5C.png"), \
        ("6 of Clubs", 6, "6C.png"), ("7 of Clubs", 7, "7C.png"), \
        ("8 of Clubs", 8, "8C.png"), ("9 of Clubs", 9, "9C.png"), \
        ("10 of Clubs", 10, "10C.png"), ("Jack of Clubs", 10, "JC.png"), \
        ("Queen of Clubs", 10, "QC.png"), ("King of Clubs", 10, "KC.png")]
    #gives length of deck
    def length(self):
        return len(self.Deck)

    #adds random cards to hands
    def createHand(self):
        hand = []
        for i in range(2):
            random.shuffle(self.Deck)
            card = self.Deck.pop()
            hand.append(card)
        return hand

    #new deck to repopulate original deck after all cards are used (shuffling deck)
    def newDeck(self):
        self.Deck = [("Ace of Hearts", 11, "AH.png"), ("2 of Hearts", 2, "2H.png"), \
        ("3 of Hearts", 3, "3H.png"), ("4 of Hearts", 4, "4H.png"), \
        ("5 of Hearts", 5, "5H.png"), ("6 of Hearts", 6, "6H.png"), \
        ("7 of Hearts", 7, "7H.png"), ("8 of Hearts", 8, "8H.png"), \
        ("9 of Hearts", 9, "9H.png"), ("10 of Hearts", 10, "10H.png"), \
        ("Jack of Hearts", 10, "JH.png"), ("Queen of Hearts", 10, "QH.png"), \
        ("King of Hearts", 10, "KH.png"), ("Ace of Spades", 11, "AS.png"), \
        ("2 of Spades", 2, "2S.png"), ("3 of Spades", 3, "3S.png"), \
        ("4 of Spades", 4, "4S.png"), ("5 of Spades", 5, "5S.png"), \
        ("6 of Spades", 6, "6S.png"), ("7 of Spades", 7, "7S.png"), \
        ("8 of Spades", 8, "8S.png"), ("9 of Spades", 9, "9S.png"), \
        ("10 of Spades", 10, "10S.png"), ("Jack of Spades", 10, "JS.png"), \
        ("Queen of Spades", 10, "QS.png"), ("King of Spades", 10, "KS.png"), \
        ("Ace of Diamonds", 11, "AD.png"), ("2 of Diamonds", 2, "2D.png"), \
        ("3 of Diamonds", 3, "3D.png"), ("4 of Diamonds", 4, "4D.png"), \
        ("5 of Diamonds", 5, "5D.png"), ("6 of Diamonds", 6, "6D.png"), \
        ("7 of Diamonds", 7, "7D.png"), ("8 of Diamonds", 8, "8D.png"), \
        ("9 of Diamonds", 9, "9D.png"), ("10 of Diamonds", 10, "10D.png"), \
        ("Jack of Diamonds", 10, "10D.png"), ("Queen of Diamonds", 10, "QD.png"), \
        ("King of Diamonds", 10, "KD.png"), ("Ace of Clubs", 11, "AC.png"), \
        ("2 of Clubs", 2, "2C.png"), ("3 of Clubs", 3, "3C.png"), \
        ("4 of Clubs", 4, "4C.png"), ("5 of Clubs", 5, "5C.png"), \
        ("6 of Clubs", 6, "6C.png"), ("7 of Clubs", 7, "7C.png"), \
        ("8 of Clubs", 8, "8C.png"), ("9 of Clubs", 9, "9C.png"), \
        ("10 of Clubs", 10, "10C.png"), ("Jack of Clubs", 10, "JC.png"), \
        ("Queen of Clubs", 10, "QC.png"), ("King of Clubs", 10, "KC.png")]

    #deals cards
    def deal(self):
        for i in range(1):
            random.shuffle(self.Deck)
            card = self.Deck.pop()
        return card
