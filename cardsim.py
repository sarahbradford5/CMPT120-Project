#Sarah Bradford
#Project 5 - card simulator
# 2020-05-11


print("Card Simulator")

import random 
class Card:
    def __init__ (self, suit, rank):
        self.suit = suit 
        self.rank = rank
        
    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

class Deck:
    def __init__ (self): #need 52 cards in deck in this instance variable
        deck = []
        suit = ""
        for x in range(1, 5):
            if x == 1:
                suit = 'spade'
            elif x == 2:
                suit = 'club'
            elif x == 3:
                suit = 'heart'
            elif x == 4:
                suit = 'diamond'
            for y in range(1, 14):
                card=""
                if y == 1:
                    card = Card(suit, "ace")
                elif y < 11:
                    card = Card(suit, str(y))
                elif y == 11:
                    card = Card(suit, "jack")
                elif y == 12:
                    card = Card(suit, "queen")
                elif y == 13:
                    card = Card(suit, "king")
                deck.append(card)
        self.deck = deck
    def shuffle(self):
        random.shuffle(self.deck)
        for z in range(len(self.deck) -1, 0, -1):
            s = random.randint(0, z)
            self.deck[z], self.deck[s] = self.deck[s], self.deck[z]
    def draw(self):
        card = self.deck.pop(0)
        x = card.getSuit() + " " + card.getRank()
        return x 
        

def main():  
    cards = Deck()
    cards.shuffle()
    for x in range(0,52):
        print(cards.draw())

main()



