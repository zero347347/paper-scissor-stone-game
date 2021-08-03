# first we are going to define two player which is computer and you
# computer is going to play it randomly
# we are to going play scissor paper stone by choosing (input)
# paper>rock, rock>scissor, scissor>paper

import random

print("We are going to play paper, scissor, stone")
print("scissor = s, paper = p, stone = rock = r")
player = []
computer = []
player = input("What's your choice: ")
game_list = ["s", "p", "r"]
computer = random.choice(game_list)
print(computer)


# paper > stone, stone > scissor, scissor > paper
def is_win(player, computer):
    if (player == "r" and computer == "s") or (player == "s" and computer == "p") or (player == "p" and computer == "r"):
        return True


# we have 3 situation when playing the game, win, tie, lose
def game_played(player, computer):
    if player == computer:
        return "It's a tie"
    elif is_win(player, computer):
        return "You won the game"
    return "You lost"

print(game_played(player, computer))