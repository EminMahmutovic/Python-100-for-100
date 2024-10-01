import random                               # Import random module and the other modules
from hangman_words import word_list         # containing a word list for our game and some
from hangman_art import stages              # ASCII art, etc.
from hangman_art import logo

lives = 6                                   # Define variable to denote number of lives before
                                            # the game is over

print(logo)                                 # Start of the game

chosen_word = random.choice(word_list)      # Choose a random starting word for hangman
print(chosen_word)

placeholder = ""                            # This block is for creating a "Placeholder" with underscores
word_length = len(chosen_word)              # to symbolize the "Writing space" for the game, equal to the
for position in range(word_length):         # number of characters in the random word.
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False                           # Set a qualification to check later to know when the game is over
correct_letters = []                        # A list whose purpose is to store the correctly guessed letters
                                            # and display them after iterations of the game.

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()                           # Make a guess

    display = ""                                                        # Variable to display of correctly guessed letters

                                                                        # The first "If" block does 3 things:
    for letter in chosen_word:
        if letter == guess:                                             # 1. If the guess is correct, it adds the correct letter
            display += letter                                           # to "display", and also adds them to the list from before.
            correct_letters.append(guess)
        elif letter in correct_letters:                                 # 2. It checks if the guess has already been guessed by
            display += letter                                           # comparing it to "correct_letters", and a message.
            print(f"You have already guessed {guess}. Guess again")
        else:                                                           # 3. If it's an incorrect guess, the display is filled with
            display += "_"                                              # and underscore instead to denote this.

    print("Word to guess: " + display)

    if guess not in chosen_word:                                                    # This "If" block deducts lives if the guesses
        lives -= 1                                                                  # are incorrect, and delivers a message.
        print(f"You guessed {guess}. You lose a life!")
        if lives == 0:                                                              # This is where the game_over variable comes into
            game_over = True                                                        # play. When you lose, based on the condition
                                                                                    # lives = 0, we set game_over = True. In this case,
            print(f"***********************YOU LOSE**********************")         # You lose.

    if "_" not in display:                                                          # In the other case where game_over = True, it occurs
        game_over = True                                                            # when there are no more underscores in the display
        print("****************************YOU WIN****************************")    # variable, you win.

    print(stages[lives]) # A reminder of how many lives are left.
