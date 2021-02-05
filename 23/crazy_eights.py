import random
from cards import Card


def init_card():
    global deck,p_hand,c_hand,up_card,active_suit
    deck = []
    for suit in range(1,5):
        for rank in range(1,14):
            new_card= Card(suit,rank)
            if new_card.rank == 8:
                new_card.value = 50
            deck.append(new_card)


    p_hand=[]
    for cards in range(0,5):
        a = random.choice(deck)
        p_hand.append(a)
        deck.remove(a)
    c_hand=[]
    for cards in range(0,5):
        a = random.choice(deck)
        c_hand.append(a)
        deck.remove(a)

    card = random.choice(deck)
    deck.remove(card)
    up_card = card
    active_suit =up_card.suit



def player_turn():
    global deck,p_hand,c_hand,up_card,active_suit
    valid_play = False
    is_eight = False
    print "\n Your hand:",
    for card in p_hand:
        print card.short_name,
    print "     Up card: ",up_card.short_name
    if up_card.rank =="8":
        print "     Suit is",active_suit
    print "What would you like to do?"
    response = raw_input("Type a card to play or 'Draw' to take a card：")
   
    while not valid_play:
        selected_card = None
        while selected_card ==None:
            if response.lower() == 'draw':
                valid_play = True
                if len(deck) >0:
                    card =random.choice(deck)
                    p_hand.append(card)
                    deck.remove(card)
                    print "You drew",card.short_name
                else:
                    print "There are no cards left in the deck"
                    blocked+=1
                return
            else:
                for card in p_hand:
                    if response.upper() == card.short_name:
                        selected_card =card
                if selected_card ==None:
                    response = raw_input("You don't have that card. Try again:")
            if selected_card.rank =='8':
                valid_play = True
                is_eight =True
            elif selected_card.suit == active_suit:
                valid_play =True
            elif selected_card.rank ==up_card.rank:
                valid_play = True

            if not valid_play:
                response = raw_input("That's not a legal play. Try again:")
        p_hand.remove(selected_card)
        up_card = selected_card
        active_suit = up_card.suit
        print "You played",selected_card.short_name
        if is_eight:
            get_new_suit()


def get_new_suit():
    global active_suit
    got_suit = False
    while not got_suit:
        suit =raw_input("Pick a suit:")
        if suit.lower() =='d':
            active_suit="Diamonds"
            got_suit= True
        elif suit.lower() =='s':
            active_suit="Spades"
            got_suit= True
        elif suit.lower() =='h':
            active_suit="Hearts"
            got_suit= True
        elif suit.lower() =='c':
            active_suit="Clubs"
            got_suit= True
        else:
            print "Not a valid suit.Try again.",
            print "You picked",active_suit

def computer_turn():
    global c_hand,deck,up_card,active_suit,blocked
    options =[]
    for card in c_hand:
        if card.rank =='8':
            c_hand.remove(card)
            up_card = card
            print " Computer played",card.short_name
            #totals:[diamonds,hearts,spades,clubs],[3,1,1,0]
            #统计花色牌数
            suit_totals = [0,0,0,0]
            for suit in range(1,5):
                for card in c_hand:
                    if card.suit_id ==suit:
                        suit_totals[suit-1]+=1
            long_suit = 0
            max_num=0
            for i in range(4):
                if suit_totals[i]>max_num:
                    print max_num
                    max_num=suit_totals[i]
                    long_suit=i
            if long_suit == 0 :active_suit="Diamonds"
            if long_suit == 1 :active_suit="Hearts"
            if long_suit == 2 :active_suit="Spades"
            if long_suit == 3 :active_suit="Clubs"
            print " Computer changed suit to ",active_suit
            return
        else:
            if card.suit == active_suit:
                options.append(card)
            elif card.rank == up_card.rank:
                options.append(card)
    if len(options)>0:
        best_play = options[0]
        for card in options:
            if card.value >best_play.value:
                best_play =card
        c_hand.remove(best_play)
        up_card=best_play
        active_suit =up_card.suit
        print " Computer played ",best_play.short_name

    else :
        if len(deck) >0:
            next_card =random.choice(deck)
            c_hand.append(next_card)
            deck.remove(next_card)
            print " Computer drew a card"
        else:
            print " Computer is blocked"
            blocked +=1
        print "Computer has %i cards left" %(len(c_hand))


done =False
p_total =c_total =0
while not done:
    game_done =False
    blocked = 0
    init_card()
    while not game_done:
        player_turn()
        if len(p_hand) ==0:
            game_done = True
            print
            print "You won!"
            p_point = 0 
            for card in c_hand:
                p_point +=card.value
            p_total += p_point
            print "You got %i points for computer's hand" % p_point
        if not game_done:
            computer_turn()
        if len(c_hand) ==0:
            game_done = True
            print
            print "Computer won!"
            c_point = 0 
            for card in p_hand:
                c_point +=card.value
            c_total += c_point
            print "You got %i points for computer's hand" % c_point
        if blocked >=2:
            game_done = True
            print "Both players blocked. GAME OVER"
            p_points = 0
            for card in c_hand:
                p_point += card.value
            p_total += p_point
            c_points = 0
            for card in p_hand:
                c_point += card.value
            c_total += c_point
            print "You got %i points for computer's hand "% p_points
            print "Computer got %i points for computer's hand "% c_points
    play_again = raw_input("Play again (Y/N)?")
    if play_again.lower().startswith('y'):
        done =False
        print "\nSo far,you have %i points "%p_total
        print "and the computer has %i points.\n"%c_total
    else:
        done=True
print "\n Final Score:"
print "You: %i     Computer:%i"%(p_total,c_total)
