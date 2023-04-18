import numpy as np
import random as rd
from card import Card

#while True:
#    if input() == "END":
#        break
#yeah = input()
t = range(2,15)
print(t)
all_cards = np.zeros((52,3))
for i in range(all_cards.shape[0]):
    all_cards[i,0] = i

colors = [" clubs ", "diamond", " spade ", " heart "]
values = ["  2  ", "  3  ", "  4  ", "  5  ", "  6  ", "  7  ", "  8  ", "  9  ", " 10  ", "Jack ", "Queen", "King ", " Ace "]
for i in range(4):
    all_cards[13*i:(13*i+13),1] = i
    all_cards[13*i:(13*i+13),2] = range(13)

def random_number_of_cards(card_stack, num_cards):
    return card_stack[rd.sample(range(card_stack.shape[0]), num_cards),:]
    #return card_stack[np.random.randint(52, size=num_cards),:]

print("all cards: \n", all_cards)
print("Your randomized hand is: \n", random_number_of_cards(all_cards, 5))

def print_card(card):
    a = int(card[2])
    print(values[a])
    print("shape: ", card.shape)
    print("Your cards are: \n")
    print(" _______ \n|{}|\n| {} |\n|_______|".format(colors[int(card[1])], values[int(card[2])]))

print_card(all_cards[50,:])