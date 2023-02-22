from typing import List
import random
import time
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank
class Deck():
    def __init__(self) -> None:
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit,rank))
                
def count_hand(hand:List[Card]):
    sum = 0
    acecount = 0
    for card in hand:
        if card.rank in ['J','Q', 'K']:
            sum+=10
        elif card.rank != 'A':
            sum+=int(card.rank)
        else:
            acecount+=1
    for _ in range(acecount):
        sum+=11 if sum+11<=21 else 1
    return sum

    
    
            
            
            
dealers_hand = []
players_hand = []
player_total = 0
dealer_total = 0
deck = Deck()
random.shuffle(deck.cards)
players_hand.append(deck.cards.pop())
players_hand.append(deck.cards.pop())
dealers_hand.append(deck.cards.pop())
dealers_hand.append(deck.cards.pop())
player_total = count_hand(players_hand)
dealer_total = count_hand(dealers_hand)
turn = 0
state = 'In Play'
action = ''
print(f"Dealer is showing: {dealers_hand[0].rank}")
print(f"Your hand is {[str(card) for card in players_hand]} for a total of {player_total}")
if player_total==21:
    state = 'blackjack' if dealer_total!=21 else 'double_blackjack'
if dealer_total==21 and state=='In Play':
    state = 'dealer_blackjack'
while state == 'In Play':
    action = ''
    #players turn
    while action not in ['h','s'] and turn==0:
        print("")
        action = input("Would you like to h/s: ")
        if action == 'h':
            players_hand.append(deck.cards.pop())
            player_total = count_hand(players_hand)
            print(f"Dealer is showing: {dealers_hand[0].rank}")
            print(f"Your hand is {[str(card) for card in players_hand]} for a total of {player_total}")
            
        if action == 's':
            turn = 1
            break
    if player_total>21:
        state = 'player_bust'
        break
    #dealers turn
    while turn==1:
        if dealer_total>=17:
            state = 'dealer_done'
            break
        dealers_hand.append(deck.cards.pop())
        dealer_total = count_hand(dealers_hand)
        print(f"Dealers hand is {[str(card) for card in dealers_hand]} for a total of {dealer_total}")
        time.sleep(1)
        if dealer_total>21:
            state = 'dealer_bust'
            break
#print cards then result
time.sleep(1)
print('\n'*10)
print(f"\nThe final hands are:\nYour hand is {[str(card) for card in players_hand]} for a total of {player_total}\nDealers hand is {[str(card) for card in dealers_hand]} for a total of {dealer_total}")   
if state == 'player_bust':
    print("Sorry, you busted")
elif state == 'dealer_bust':
    print("Dealer busted you win")
elif state == 'blackjack':
    print("Congrats you win with a blackjack")
elif state == 'double_blackjack':
    print("Unlucky double blackjack, push")
elif state == 'dealer_blackjack':
    print("Dealer has blackjack, you lose")
elif state == 'dealer_done':
    if(player_total>dealer_total):
        print("You win")
    elif(player_total<dealer_total):
        print("Sorry you lose")
    else:
        print("Result is a push")