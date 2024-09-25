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

if your_move_index >= 3 or your_move_index < 0:
    print("Invalid Input. Try Again.")
elif your_move_index == 0 and computer_move_index == 2:
    print("You Win!")
elif computer_move_index == 0 and your_move_index == 2:
    print("You Lose!")
elif your_move_index > computer_move_index:
    print("You Win!")
elif computer_move_index > your_move_index:
    print("You Lose")
elif your_move_index == computer_move_index:
    print("It's a Draw")




