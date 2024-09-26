# ASCI art of rock-paper-scissors stored as variables
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

# Index     0       1       2
actions = [rock, paper, scissors] #List of actions

# Index of move
computer_move_index = random.randint(0,2) #Index of computer move
your_move_index = int(input("What do you choose? Type 0 for Rock, "
                 "1 for Paper, and 2 for Scissors\n")) #Index of your move

# Moves
computer_move = actions[computer_move_index] #Computer's move
your_move = actions[your_move_index] #Your move

print("You Chose")
print(your_move)
print("The Computer chose")
print(computer_move)

# All possibilities
if your_move_index >= 3 or your_move_index < 0:             # If your move is outside the interval
    print("Invalid Input. Try Again.")                      # 0-2, i.e., 3 or bigger or less than
                                                            # 0, it's invalid input

elif your_move_index == 0 and computer_move_index == 2:     # Before we can generalize the rule for
    print("You Win!")                                       # the game, seen in line __, we need to
elif computer_move_index == 0 and your_move_index == 2:     # account for two exceptions, where the
    print("You Lose!")                                      # rule won't apply, lines 53-56.

elif your_move_index > computer_move_index:                 # Now we can generalize the rules of the
    print("You Win!")                                       # game, if the your_move_index is larger
elif computer_move_index > your_move_index:                 # than the computer_move_index, or vice
    print("You Lose")                                       # versa, that party wins.

elif your_move_index == computer_move_index:                # If the input is the same, it's a draw!
    print("It's a Draw")




