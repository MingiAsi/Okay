#-------------------------------------------------------------------------------
# Name:        Blackjack game simulator
# Purpose:     
#
# Created:     22/06/2014
# Copyright:   (c) Copyright Mic 2014
# Licence:     GNU GPL
#
#
#     This software is distributed under the GNU GPL license
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    If you need to contact the author of this program, please fill in the
#    contact form at http://firsttimeprogrammer.blogspot.it/p/contacts.html
#-------------------------------------------------------------------------------


# IMPORTANT NOTE: Before running the script, please set up the images_url to the
# local folder where pictures are located.


import random
import easygui

global double_down
double_down = False

################################################################################
#SET UP : Set the path to the local folder where pictures are located before
#running the script
images_url = "C:\\users\\Paul\\desktop\\New folder (3)\\"
################################################################################

# A 52 cards deck for blackjack
deck = ["A","A","A","A",10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,8,8,8,8,7,7,7,7,6,6,6,6,5,5,5,5,4,4,4,4,3,3,3,3,2,2,2,2]


#This function modifies the player's available balance according to bet size and the outcome of a game
def assign_score_player(bet_size, player_available):
    if player_win and not p_blackjack:
        player_available += bet_size
    elif player_win and p_blackjack:
        player_available += 1.5*bet_size
    elif not player_win and not tie:
        player_available -= bet_size
    elif tie:
        pass
    return player_available


#This function modifies the dealer's available balance according to bet size and the outcome of a game
def assign_score_casino(bet_size, casino_available):
    if player_win and not p_blackjack:
        casino_available -= bet_size
    elif player_win and p_blackjack:
        casino_available -= 1.5*bet_size
    elif not player_win and not tie:
        casino_available += bet_size
    elif tie:
        pass
    return casino_available


#This function sets the value of an ace to 1 or 11 according to Blackjack rules
def set_aces(hand_to_set):
    if "A" not in hand_to_set:
        return hand_to_set
    else:
        counter_of_aces = hand_to_set.count("A")

        if counter_of_aces == 1:
            hand_to_set.remove("A")
            partial_sum = sum(hand_to_set)
            if partial_sum <= 10:
                hand_to_set.append(11)
                return hand_to_set
            else:
                hand_to_set.append(1)
                return hand_to_set
        elif counter_of_aces == 2:
            hand_to_set.remove("A")
            hand_to_set.remove("A")
            hand_to_set.append(1)
            partial_sum = sum(hand_to_set)
            if partial_sum <= 10:
                hand_to_set.append(11)
                return hand_to_set
            else:
                hand_to_set.append(1)
                return hand_to_set
        elif counter_of_aces == 3:
            hand_to_set.remove("A")
            hand_to_set.remove("A")
            hand_to_set.remove("A")
            hand_to_set.append(1)
            hand_to_set.append(1)
            partial_sum = sum(hand_to_set)
            if partial_sum <= 10:
                hand_to_set.append(11)
                return hand_to_set
            else:
                hand_to_set.append(1)
                return hand_to_set
        elif counter_of_aces == 4:
            hand_to_set.remove("A")
            hand_to_set.remove("A")
            hand_to_set.remove("A")
            hand_to_set.remove("A")
            hand_to_set.append(1)
            hand_to_set.append(1)
            hand_to_set.append(1)
            partial_sum = sum(hand_to_set)
            if partial_sum <= 10:
                hand_to_set.append(11)
                return hand_to_set
            else:
                hand_to_set.append(1)
                return hand_to_set



#This function deals with the case in which another ace has been dealt and added to a hand
def convert_aces(hand_to_convert):
    if 11 not in hand_to_convert:
        return hand_to_convert
    else:
        if sum(hand_to_convert) > 21:
            hand_to_convert.remove(11)
            hand_to_convert.append(1)
            return hand_to_convert
        else:
            return hand_to_convert

#This function removes dealt cards from the deck, since they are no longer available to be dealt
def remove_deck(hand_to_remove):
    for i in hand_to_remove:
        deck.remove(i)
    return deck

#This function generates a hand of cards for the player
def player_hand():
    p_hand = random.sample(deck, 2)
    remove_deck(p_hand)
    p_hand = set_aces(p_hand)
    return p_hand

#This function generates a hand of cards for the dealer
def dealer_hand():
    d_hand = random.sample(deck, 2)
    remove_deck(d_hand)
    d_hand = set_aces(d_hand)
    return d_hand

#This function asks for an input by the player, generates a new dealt card if asked, and checks if the player has gone bust
def player_new_card(p_hand, d_hand):
    card = "yes"
    global p_busted
    p_busted = False
    global double_down

    while (card == "yes") and (sum(p_hand) != 21):

        options = ["Double down", "yes", "no"]

        if len(p_hand) == 2:
            card = easygui.buttonbox(msg = "Your turn! Double down, hit or stay?\nhit: yes\nstay: no\n"+ "Your hand: " + str(p_hand) + " and dealer's: " + str(d_hand[0]), title = "Blackjack", choices = options, image = images_url + "imm.gif" )
            if card == "Double down":
                double_down = True
                new_card = random.sample(deck, 1)
                p_hand.append(new_card[0])
                remove_deck(new_card)
                p_hand = set_aces(p_hand)
                p_hand = convert_aces(p_hand)
                if sum(p_hand) > 21:
                    print("Busted!! " + "Your hand: " + str(p_hand))
                    p_busted = True
                    break
                else:
                    print("Your hand: " + str(p_hand))
                    return p_hand
            elif card == "yes":
                new_card = random.sample(deck, 1)
                p_hand.append(new_card[0])
                remove_deck(new_card)
                p_hand = set_aces(p_hand)
                p_hand = convert_aces(p_hand)
                double_down = False
                if sum(p_hand) > 21:
                    print("Busted!! " + "Your hand: " + str(p_hand))
                    p_busted = True
                    break
            else:
                print("Your hand: " + str(p_hand))
                double_down = False
                return p_hand

        if len(p_hand) > 2:
            options.remove("Double down")
            card = easygui.buttonbox(msg = "Your turn! Hit or stay?\nhit: yes\nstay: no\n"+ "Your hand: " + str(p_hand) + " and dealer's: " + str(d_hand[0]), title = "Blackjack", choices = options, image = images_url + "imm.gif" )
            if card == "yes":
                new_card = random.sample(deck, 1)
                p_hand.append(new_card[0])
                remove_deck(new_card)
                p_hand = set_aces(p_hand)
                p_hand = convert_aces(p_hand)
                double_down = False
                if sum(p_hand) > 21:
                    print("Busted!! " + "Your hand: " + str(p_hand))
                    p_busted = True
                    break
            else:
                print("Your hand: " + str(p_hand))
                double_down = False
                return p_hand
    return p_hand

#This function generates a new card for the dealer according to Bj rules
def dealer_new_card(d_hand):
    global d_busted
    d_busted = False
    while sum(d_hand) < 16:
        new_card = random.sample(deck,1)
        d_hand.append(new_card[0])
        remove_deck(new_card)
        d_hand = set_aces(d_hand)
        d_hand = convert_aces(d_hand)
        if sum(d_hand) > 21:
            print("You won!!" + " Dealer's hand: " + str(str(d_hand)))
            d_busted = True
    return d_hand

#This function select the winner according to Bj rules
def who_wins(p_hand, d_hand):
    global player_win
    global tie
    global p_blackjack
    global d_blackjack
    if p_busted == True:
        print("Busted, you lost")
        easygui.msgbox(msg = "Busted, you lost!! Here's your hand: "+ str(p_hand) + "and the dealer's: " + str(d_hand), title = "You lost", image = images_url + "lost.gif")
        player_win = False
        tie = False
        p_blackjack = False
    elif d_busted == True:
        print("Dealer busted, congratulations you won!")
        easygui.msgbox(msg = "Dealer busted, congratulations you won! Here's your hand: "+ str(p_hand) + "and the dealer's: " + str(d_hand), title = "You won", image = images_url + "win.gif")
        player_win = True
        tie = False
        p_blackjack = False
    elif((sum(p_hand) == 21) and (len(p_hand) == 2) and (sum(p_hand) != sum(d_hand))):
        print("BLACKJACK, you won!! " + " Here's your hand: " + str(p_hand) + "and the dealer's: " + str(d_hand))
        easygui.msgbox(msg = "BLACKJACK, you won!! Congratulations you won! Here's your hand: "+ str(p_hand) + "and the dealer's: " + str(d_hand), title = "You won", image = images_url + "bj.gif")
        player_win = True
        tie = False
        p_blackjack = True
    elif((sum(d_hand) == 21) and (len(d_hand) == 2) and (sum(d_hand) != sum(p_hand))):
        print("Dealer has BLACKJACK, you lost!! " + " Here's your hand: " + str(p_hand) + "and the dealer's: " + str(d_hand))
        easygui.msgbox(msg = "Dealer has BLACKJACK, you lost!! Here's your hand: "+ str(p_hand) + "and the dealer's: " + str(d_hand), title = "You lost", image = images_url + "lost.gif")
        player_win = False
        tie = False
        p_blackjack = False
    elif sum(p_hand) > sum(d_hand):
        print("You won, here's your hand: " + str(p_hand) + "and the dealer's: " + str(d_hand))
        easygui.msgbox(msg = "You won, here's your hand: "+ str(p_hand) + "and the dealer's: " + str(d_hand), title = "You won", image = images_url + "win.gif")
        player_win = True
        tie = False
        p_blackjack = False
    elif((sum(p_hand) == sum(d_hand)) and (len(p_hand) == len(d_hand))):
        print("Tie, here's your hand: " + str(p_hand) + "and the dealer's: " + str(d_hand))
        easygui.msgbox(msg = "Tie, try again! Here's your hand: "+ str(p_hand) + "and the dealer's: " + str(d_hand), title = "Tie", image = images_url + "draw.gif")
        player_win = False
        tie = True
        p_blackjack = False
    elif((sum(p_hand) == sum(d_hand)) and (len(d_hand) != 2) and (len(p_hand) != 2)):
        print("Tie, here's your hand: " + str(p_hand) + "and the dealer's: " + str(d_hand))
        easygui.msgbox(msg = "Tie, try again! Here's your hand: "+ str(p_hand) + "and the dealer's: " + str(d_hand), title = "Tie", image = images_url + "draw.gif")
        player_win = False
        tie = True
        p_blackjack = False
    else:
        print("You lost, here's your hand: " + str(p_hand) + "and the dealer's: " + str(d_hand))
        easygui.msgbox(msg = "Dealer beat you, you lost! Here's your hand: "+ str(p_hand) + "and the dealer's: " + str(d_hand), title = "You lost", image = images_url + "lost.gif")
        player_win = False
        tie = False
        p_blackjack = False



#Basic variables can be set as you please (except for continue_play which must be 1 in order for the loop to start)
continue_play = 1
max_bet = 100
min_bet = 10
player_available = 10000
casino_available = 10000


while continue_play == 1:

    #The player is asked if they want to continue the game, if yes continue_play becomes 1, otherwise it becomes 0
    continue_play = easygui.ccbox(msg = "Play again? yes/no", title = "Blackjack", image = images_url + "game.gif")

    #If the player does not want to continue, the game is ended
    if continue_play == 0:
        break

    #The deck is restored after a game
    deck = ["A","A","A","A",10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,8,8,8,8,7,7,7,7,6,6,6,6,5,5,5,5,4,4,4,4,3,3,3,3,2,2,2,2]


    #The player is asked to place a bet according to some parameters
    bet_size = easygui.integerbox(msg = "Enter a bet:\n maximum bet: " +str(max_bet) + "\n minimum bet: " + str(min_bet) + "\n" + "Available balance: " + str(player_available), title='Place a bet', default='', lowerbound = min_bet, upperbound = max_bet, image = images_url + "place.gif")

    #If the player clicks "cancel" the game stops
    if str(type(bet_size)) == "<class 'int'>":
        pass
    else:
        break

    #A new hand is generated
    p1_hand = player_hand()
    print("Your hand: " + str(p1_hand))

    #Only one of the two dealer's card is shown according to Bj rules
    d1_hand = dealer_hand()
    print("Dealer's hand: " + str(d1_hand[0]))

    #The game goes on
    p1_hand = player_new_card(p1_hand, d1_hand)
    d1_hand = dealer_new_card(d1_hand)

    if double_down:
        bet_size = 2*bet_size

    #Eventually we find the winner
    who_wins(p1_hand, d1_hand)

    #Available balances are set according to the result of the game
    player_available = assign_score_player(bet_size, player_available)
    casino_available = assign_score_casino(bet_size, casino_available)
    print("Your balance: "+str(player_available))
    print("Dealer's balance: "+str(casino_available))

    #If player's available balance is 0 or less than 0 the game is over
    if player_available <= 0:
        easygui.msgbox(msg = "You lost all your available balance", title = "Sorry, you lost", image = images_url + "dog.gif")
        break









