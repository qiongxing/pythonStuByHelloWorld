import random
from cards import Card

deck = []
for suit_id in range(1,5):
    for rank_id in range(1,14):
        new_card= Card(suit,rank)
        deck.append(new_card)

hand=[]
for cards in range(0,5):
    a = random.choice(deck)
    hand.append(a)
    deck.remove(a)

print 
for card in hand:
    print card.short_name,'=',card.long_name," Value:",card.value