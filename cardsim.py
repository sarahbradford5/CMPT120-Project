#Sarah Bradford
#Project 5

#52 cards in a deck 
    #for each suit there must be 13 cards with distinct rank

#getSuit -> returns what the suit card is
#getRank -> returns waht the rank card it 

print("Card Simulator Game")

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

    
def main():
    cards = Deck()
    deck = cards.deck
    print(len(deck))
    for c in deck:
        print(c.getSuit() + " " + c.getRank())
    
main()
