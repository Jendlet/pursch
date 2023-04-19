import numpy as np
import random as rd
from card import Card
from colorama import Fore, Style
import sys

#while True:
#    if input() == "END":
#        break
#yeah = input()

all_cards = np.zeros((52,3))
colors = ["clubs", "diamd", "spade", "heart"]
values = ["  2  ", "  3  ", "  4  ", "  5  ", "  6  ", "  7  ", "  8  ", "  9  ", " 10  ", "Jack ", "Queen", "King ", " Ace "]

for i in range(4):
    all_cards[13*i:(13*i+13),0] = range(13*i,13*i+13)
    all_cards[13*i:(13*i+13),1] = i
    all_cards[13*i:(13*i+13),2] = range(13)

def random_number_of_cards(card_stack, num_cards):
    if num_cards > 5 or num_cards < 0:
        raise Exception("You can only select between 0 and 5 new cards!")
        
    random_card_ids = rd.sample(range(card_stack.shape[0]), num_cards)
    random_set_of_cards = card_stack[random_card_ids,:]
    card_stack_new = card_stack.copy()

    for i in range(num_cards):
        index_to_delete = np.where(card_stack_new[:,0] == random_card_ids[i])
        card_stack_new = np.delete(card_stack_new, index_to_delete, 0)
    return [random_set_of_cards, card_stack_new]
    #return card_stack[np.random.randint(52, size=num_cards),:]

def print_card(card):
    CRED = '\033[91m'
    CEND = '\033[0m'

    if (colors[int(card[1])] == "heart" or colors[int(card[1])] == "diamd"):
        card_color = CRED+colors[int(card[1])]+CEND
    else:
        card_color = colors[int(card[1])]

    print("\n\n _______ \n| {} | \n| {} |".format(card_color, values[int(card[2])])+"\n|       |\n|       |\n|_______|")


def print_hand(hand, player):
    CRED = '\033[91m'
    CEND = '\033[0m'
    
    card_colors = [""]*5
    for i in range(5):
        if (colors[int(hand[i,1])] == "heart" or colors[int(hand[i,1])] == "diamd"):
            card_colors[i] = CRED+colors[int(hand[i,1])]+CEND
        else:
            card_colors[i] = colors[int(hand[i,1])]

    print("\n\n _______   _______   _______   _______   _______ \n| {} | | {} | | {} | | {} | | {} |\n| {} | | {} | | {} | | {} | | {} |".
          format(card_colors[0],card_colors[1],card_colors[2],card_colors[3],card_colors[4],
                 values[int(hand[0,2])],values[int(hand[1,2])],values[int(hand[2,2])],values[int(hand[3,2])],values[int(hand[4,2])])
          +"\n|       | |       | |       | |       | |       |\n|       | |       | |       | |       | |       |\n|_______| |_______| |_______| |_______| |_______|")
    print("hand of player " + player)

print("Deals first five cards...")
num_players = 1
players_hands = np.zeros((num_players, 5, 3))
current_card_stack = all_cards.copy()
for i in range(players_hands.shape[0]):
    random_cards, current_card_stack = random_number_of_cards(current_card_stack, 5)
    players_hands[i,:,:] = random_cards
    print_hand(players_hands[i,:,:], player=str(i+1))
    

#print_card(players_hands[0,0,:])

def discard(hand, cards_to_discard):
    #cards_to_discard_int = int(cards_to_discard)
    for i in range(len(cards_to_discard)):
        if cards_to_discard[i] > 5 or cards_to_discard[i] < 0:
            raise Exception("You can only select your cards between 1 and 5!")
        hand_without_discarded_cards = np.delete(hand, cards_to_discard[i], 0)
    return hand_without_discarded_cards

print("\n\nWhat cards would you like to discard?\n")
print_hand(players_hands[0,:,:], player=str(0+1))
#cards_to_discard = input("What cards would you like to discard?\n")
#cards_to_discard = sys.stdin.read()
#if(cards_to_discard[-1] == '\n'):
#    cards_to_discard = cards_to_discard[:-1]
cards_to_discard = [int(x) for x in input().split()]
cards_to_discard.sort(reverse=True)

new_hand = discard(players_hands[0,:,:], cards_to_discard)
print_card(new_hand[0,:])
print_card(new_hand[1,:])
print_card(new_hand[2,:])
print_card(new_hand[3,:])
print_card(new_hand[4,:])
