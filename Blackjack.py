#Blackjack
#Written by Ana Knighten and Ali Purdum
#This program lets you play a simulation of the card game Blackjack
#Time spent on project: 24 hours over 6 days

from graphics import *
import time
from classDeck import *
from classPlayer import *
from classDealer import *
from classButton import *

#
def drawHit(text, win):
    drawhit = Text(Point(180, 300), text).draw(win)
    drawhit.setSize(14)
    return drawhit

#Draws how much money the player has
def money(player, win):
    totalmoney = Text(Point(90, 260), "You have $" + str(player.money)).draw(win)
    totalmoney.setSize(14)
    return totalmoney

#Lets player enter amount of money to bet
def drawBet(player, quitButton, win):
    text = Text(Point(170, 290), "How many dollars would you like to bet?").draw(win)
    text.setSize(14)
    enter = Text(Point(170, 310), "Click anywhere to enter your bet.").draw(win)
    enter.setSize(14)
    inputbox = (Entry(Point(360, 290), 4))
    inputbox.draw(win)
    click = win.getMouse()

    if quitButton.clicked(click):
        inputbox.undraw()
        drawQuit("Thanks for Playing!", win)
    betMoney = inputbox.getText()

    try:
        betMoney = int(betMoney)
    #accounts for accidental click before entering bet
    except ValueError:
        click = win.getMouse()
        betMoney = inputbox.getText()
        betMoney = int(betMoney)
    #checks that you bet valid amount
    if betMoney <= 0 or betMoney >= player.money:
        inputbox.undraw()
        text.undraw()
        enter.undraw()
        invalidbet = Text(Point(185, 290), "Please input a value below " + str(player.money) + " and above 0.").draw(win)
        invalidbet.setSize(14)
        time.sleep(2)
        invalidbet.undraw()
        return drawBet(player, quitButton, win)

    enter.undraw()
    text.undraw()
    inputbox.undraw()
    return betMoney

#Draws winner of round
def drawText(text, win):
    time.sleep(1)
    popup = Rectangle(Point(0,0), Point(500, 500)).draw(win)
    popup.setFill("mediumorchid")
    message = Text(Point(250, 250), text)
    message.setSize(20)
    message.draw(win)
    time.sleep(5)
    message.undraw()
    playagainmessage = Text(Point(250, 250),"Click the Deal button to deal a new hand. \n Click the Quit button to quit.").draw(win)
    playagainmessage.setSize(20)
    time.sleep(4)
    playagainmessage.undraw()
    popup.undraw()

#Draws flashing text to let user know they got a blackjack
def drawBlackjack(win):
    bjpopup = Rectangle(Point(0,0), Point(500, 500)).draw(win)
    bjpopup.setFill("crimson")
    message = Text(Point(250,250), "You Got A Blackjack!")
    message.setSize(24)
    #flashes messsage
    for i in range(15):
        time.sleep(0.15)
        if i % 2 == 0:
            message.draw(win)
        else:
            message.undraw()
    message.undraw()
    playagainmessage = Text(Point(250, 250),"Click the Deal button to deal a new hand. \n Click the Quit button to quit.").draw(win)
    playagainmessage.setSize(20)
    time.sleep(4)
    playagainmessage.undraw()
    bjpopup.undraw()

#Lets user know they have run out of money to bet
def noMoney(player, win):
    if player.money <= 0:
        drawQuit("Sorry! You ran out of money to bet!", win)

#Draws quit message
def drawQuit(text, win):
    popup = Rectangle(Point(0,0), Point(500, 500)).draw(win)
    popup.setFill("mediumorchid")
    message = Text(Point(250, 250), text)
    message.setSize(24)
    message.draw(win)
    time.sleep(3)
    exit()

#Checks for blackjack
def checkScore(player, dealer):
    if player.score == 21:
        return True
    if dealer.score == 21:
        return True
    if player.score > 21:
        return True
    if dealer.score > 21:
        return True
    else:
        return False

#Draws results for final score of hand
def finalScore(player, dealer, deck, dealButton, quitButton, betMoney, win, playerImageList, dealerImageList, totalmoney, drawplayerscore, drawdealerscore):
    if player.score == 21:
        player.winBet(betMoney)
        drawBlackjack(win)

    if dealer.score == 21:
        player.loseBet(betMoney)
        noMoney(player, win)
        drawText("Sorry! You lose.\n The dealer got a Blackjack.\n\n You now have " + str(player.money) + " dollars!", win)

    if player.score < dealer.score < 21:
        player.loseBet(betMoney)
        noMoney(player, win)
        drawText("Sorry. Your score isn't higher than the dealer.\n You lose.\n\n You now have " + str(player.money) + " dollars!", win)

    if dealer.score < player.score < 21:
        player.winBet(betMoney)
        drawText("Congratulations!\n Your score is higher than the dealer.\n You win!\n\n You now have " + str(player.money) + " dollars!", win)

    if player.score == dealer.score:
        drawText("It's a Draw!", win)

    if player.score > 21:
        player.loseBet(betMoney)
        noMoney(player, win)
        drawText("Sorry! You busted.\n You lose.\n\n You now have " + str(player.money) + " dollars!", win)

    elif dealer.score > 21:
        player.winBet(betMoney)
        drawText("Dealer busted!\n You win!\n\n You now have " + str(player.money) + " dollars!", win)
    playAgain(player, dealer, deck, dealButton, quitButton, win, playerImageList, dealerImageList, totalmoney, drawplayerscore, drawdealerscore)

#Lets user play another hand
def playAgain(player, dealer, deck, dealButton, quitButton, win, playerImageList, dealerImageList, totalmoney, drawplayerscore, drawdealerscore):
    point = win.getMouse()
    #deals new cards
    if dealButton.clicked(point) == True:
        player.newHand(deck)
        dealer.newHand(deck)
        totalmoney.undraw()
        drawplayerscore.undraw()
        drawdealerscore.undraw()
        player.undrawCard(win, playerImageList)
        dealer.undrawCard(win, dealerImageList)
        return True

    elif quitButton.clicked(point) == True:
        drawQuit("Thanks for Playing!", win)
    else:
        playAgain(player, dealer, deck, dealButton, quitButton, win, playerImageList, dealerImageList, totalmoney, drawplayerscore, drawdealerscore)


#Runs game
def main():
    # Creates the window
    win = GraphWin("Blackjack", 500, 500)
    win.setBackground("brown")
    # Draw the table
    table = Rectangle(Point(20, 100), Point(480,480))
    table.setFill("darkgreen")
    table.draw(win)
    #Buttons
    dealButton = Button("Deal", Point(20,30), Point(125,80), Point(72.5, 55))
    dealButton.drawButton(win)
    hitButton = Button("Hit", Point(145, 30), Point(245,80), Point(195,55))
    hitButton.drawButton(win)
    stayButton = Button("Stay", Point(260, 30), Point(360, 80), Point(310, 55))
    stayButton.drawButton(win)
    quitButton = Button("Quit", Point(380, 30), Point(480, 80), Point(430, 55))
    quitButton.drawButton(win)
    #card deck
    deck = Deck()
    player = Player(deck.createHand(), deck, win)
    dealer = Dealer(deck.createHand(), deck, win)

    while playAgain != False:
        playerImageList = player.drawCard(win)
        dealerImageList = dealer.drawCard(win)
        player_score = player.addScore(player.hand)
        dealer_score = dealer.addScore(dealer.hand)
        drawplayerscore = player.drawScore(win)
        totalmoney = money(player, win)
        betMoney = drawBet(player, quitButton, win)
        #repopulates deck
        if deck.length() < 7:
            deck.newDeck()
        player_input = "a"
        cScore = checkScore(player, dealer)

        while cScore == False:
            drawhit = drawHit("Click on the Hit, Stay or Quit buttons to play!", win)
            point = win.getMouse()
            drawhit.undraw()
            #hits player with another card
            if hitButton.clicked(point) == True:
                player.hit(deck)
                player_score = player.addScore(player.hand)
                player.undrawCard(win, playerImageList)
                playerImageList = player.drawCard(win)
                drawplayerscore.undraw()
                drawplayerscore = player.drawScore(win)
                cScore = checkScore(player, dealer)
            #stops player turn and does dealer turn
            if stayButton.clicked(point) == True:
                while dealer.score < 17:
                    dealer.hit(deck)
                    dealer_score = dealer.addScore(dealer.hand)
                cScore = checkScore(player, dealer)
                dealer_score = dealer.addScore(dealer.hand)
                cScore = True
            #ends game
            if quitButton.clicked(point) == True:
                drawQuit("Thanks for Playing!", win)
        dealerImageList = dealer.drawAllCard(win)
        drawdealerscore = dealer.drawScore(win)
        #draws final scores
        finalScore(player, dealer, deck, dealButton, quitButton, betMoney,
        win, playerImageList, dealerImageList, totalmoney, drawplayerscore,
        drawdealerscore)



main()
