import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self) -> str:
        return self.rank + " of " + self.suit
class Deck:
    def __init__(self) -> None:
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
        self.lastcard = self.all_cards[-1]
        
    def shuffle(self):
        random.shuffle(self.all_cards)
        self.set_last_card()
    def deal(self):
        return self.all_cards.pop(0)
    def set_last_card(self):
        self.lastcard = self.all_cards[-1]
class Player:
    def __init__(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()
    def deck_length(self):
        return len(self.deck.all_cards)
    
def append_cards(card1:Card,card2:Card,cards:list):
    if card1 not in cards:
        cards.append(card1)
    if card2 not in cards:
        cards.append(card2)
    
        
def duel(player1: Player,player2: Player):
    card1 = player1.deck.deal()
    card2 = player2.deck.deal()
    print(str(card1) + " vs. " + str(card2))
    
    tmp = [card1,card2]
    random.shuffle(tmp)
    if(card1.value>card2.value):
        for card in tmp:
            player1.deck.all_cards.append(card)
        player1.deck.set_last_card()
    elif(card1.value<card2.value):
        for card in tmp:
            player2.deck.all_cards.append(card)
        player2.deck.set_last_card()
    else:
        war(player1,player2,[card1,card2])
    
def war(player1: Player, player2: Player, warcards): 
    print("in war")
    cards = warcards
    for _ in range(0,3):
        if(player1.deck_length()>1):
            cards.append(player1.deck.deal())
        if(player2.deck_length()>1):
            cards.append(player2.deck.deal())
            
    card1 = player1.deck.deal() if player1.deck_length()>0 else player1.deck.lastcard
    card2 = player2.deck.deal() if player2.deck_length()>0 else player2.deck.lastcard
    print(str(card1) + " vs. " + str(card2))
    if(card1.value>card2.value):
        append_cards(card1,card2,cards)
        random.shuffle(cards)
        for card in cards:
            player1.deck.all_cards.append(card)
        player1.deck.set_last_card()
            
    elif(card1.value<card2.value):
        append_cards(card1,card2,cards)
        random.shuffle(cards)
        for card in cards:
            player2.deck.all_cards.append(card)
        player2.deck.set_last_card()
    else:
        append_cards(card1,card2,cards)
        war(player1,player2,cards)
        
player1_score = 0
player2_score = 0
for i in range(0,100):
    player1 = Player()
    player2 = Player()
    while(player1.deck_length()>0 and player2.deck_length()>0):
        duel(player1,player2)
    print(str(player1.deck_length()) + " " + str(player2.deck_length()))
    if(player1.deck_length()>player2.deck_length()):
        print("Player1 wins")
        player1_score+=1
        
    else:
        print("Player2 wins")
        player2_score+=1
print("Player1: " + str(player1_score) + " Player2: "+ str(player2_score))
        

    
    