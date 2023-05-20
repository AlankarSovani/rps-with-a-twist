# rock paper scissors game with a twist

import random
import time

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif player_choice == "rock":
        if computer_choice == "paper":
            return "Computer"
        else:
            return "Player"
    elif player_choice == "paper":
        if computer_choice == "scissors":
            return "Computer"
        else:
            return "Player"
    elif player_choice == "scissors":
        if computer_choice == "rock":
            return "Computer"
        else:
            return "Player"
    else:
        return "Error"

deck = []
for i in range(4):
    deck.append('rock')
    deck.append('paper')
    deck.append('scissors')
random.shuffle(deck)

print('Welcome to Rock Paper Scissors!')
time.sleep(1)
print('You will be playing against the computer.')
time.sleep(1)
print('You will be dealt 3 cards, and 3 cards from the deck will be revealed.')
time.sleep(1)
print('The winner will be determined by the rules of Rock Paper Scissors.')
time.sleep(1)

# deal cards
player_hand = deck[:3]
computer_hand = deck[3:6]
deck = deck[6:]
win_count = 0
tie_count = 0
for i in range(3): 
    player_choice = ""
    print("Your hand: " + str(player_hand))
    time.sleep(1)
    print("Revealed cards: " + str(deck[:3]))
    time.sleep(1)
    print("Score: " + str(win_count) + "\n")
    time.sleep(1)
    player_choice = input("Choose a card to play: ")
    player_hand.remove(player_choice)
    # computer's turn
    computer_choice = random.choice(computer_hand)
    computer_hand.remove(computer_choice)
    print("Computer played: " + computer_choice)
    # determine winner
    winner = determine_winner(player_choice, computer_choice)
    if winner == "Player":
        win_count += 1
    elif winner == "Tie":
        tie_count += 1
    print(winner + " wins!")
    time.sleep(1)
# determine winner of game
if win_count > 1:
    print("You win!")
elif win_count + tie_count == 3:
    print("Tie!")
else:
    print("Computer wins!")
