#ask how much to bet?
#user starts with $100
#dealer draws cards within 1-21 cards
#player is given 2 cards within 1-21 cards
import random

class bj():
    def __init__(self,cash=100,p_cards =[]):
        self.cash = cash
        self.p_cards = p_cards
        
    def placebet(self):
        print("BlackJack")
        print("Current Funds: " + str(self.cash))
        while True:
            self.bet = int(input("How much do you want to bet? "))
            if (self.bet <= self.cash) and (self.bet >= 1):
                break
            else:
                print("You can only bet from 1 to {}".format(self.bank()))
        return self.bet
        
    def bank(self):          
        return self.cash

    def draw_cards(self):
        if len(self.p_cards) ==0:
            #print(str(len(self.p_cards)) + " string thingy")
            self.p_cards = [random.randint(1,10) for i in range(2)]
            print(self.p_cards)
            print("current total: "+ str(self.cardmath()))
        else:
            self.p_cards.append(random.randint(1,10))
        return self.p_cards
        
    def askplayer(self):
        value = int(input("do you want another card? 1 or 0 "))
        print(value)
        while True:
            if (value > 1 or value < 0):
                value = input("type only: 1 or 0 ")
            else:
                break               
        if value == 1:
            self.draw_cards()
            print(self.p_cards)
            tot =self.cardmath()
            print("current total: "+ str(tot))
            if tot < 21:
                self.askplayer()
            else:
                print("total exceeded")
                return None 
        else:
            return None     
            
    def cardmath(self):
        total = 0   
        for i in self.p_cards:
            total += i
        #print("total: " + str(total))
        return total
                              
    def dealer(self):
        self.draw_cards()
        while True:
            current_sum = self.cardmath()
            print("current total: "+ str(current_sum))
            if current_sum >= 16:
                break
            else:
                self.draw_cards()
                print(self.p_cards)
    
    def reset(self):
        self.p_cards = []  

    def playerwon(self):
        print("Player wins")
        self.cash += self.bet
    
    def playerlost(self):
        print("Dealer wins")
        self.cash -= self.bet
 
def valid_input(value):
    while True:
        if (value > 1 or value < 0):
            value = int(input("type only: 1 or 0 "))
        else:
            return value     
 
def compare(play, deal):
    if play < 21 and deal <21:
        if deal> play:               
            return player.playerlost()
        elif play > deal: 
            return player.playerwon()
    if play == deal:
        return player.playerlost()
    if deal == 21 and play == 21 :
        return player.playerlost()
    if deal == 21:
        return player.playerlost()
    if play == 21:
        return player.playerwon()
    if play > 21:
        return player.playerlost()
    if deal > 21:
        return player.playerwon()

player = bj()
dealer = bj()
while player.bank() >0:
    player.bank()
    player.placebet()
    while True:
        player.draw_cards()
        x=player.askplayer()
        if x == None:
            break
    print("********************Dealers Turn**********************")
    dealer.dealer()
    print("done")
    
    # win/lose condition
    play = player.cardmath()
    deal = dealer.cardmath()
    print("Player total: " + str(play))
    print("Dealer total: " + str(deal))
    compare(play,deal)
    print("Your current balance: " + str(player.bank()))
    print("---------------------Ready for New Game------------------------------------")
    replay = int(input("Do you want to keep playing? 1 or 0 "))
    replay = valid_input(replay)
    if replay == 0:
        break
    elif player.bank() > 0:
        player.reset()
        dealer.reset()
    else:
        print("insufficient funds")
        print(player.bank())
        print("bye looooooo$$$$$$$$$$$$$er")
    
    
    
    
    
