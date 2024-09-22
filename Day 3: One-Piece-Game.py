print('''

           __..--.                                   _.._
    _..--''_______|-._____  ______________________|``  __``--.._
   '-.-..---..---..---..--''.---..---..---..---..---..---..---.-'
     |_::___::___::___::___::___::___::___::___::___::___::___|
     |________________________________________________________|
     '.--.':'.--.' '.--.'  '.--.'  '.--.'  '.--.' '.--.' '.--.'
      |''|.|.|''|-. |''|    |''|    |''|    |''|   |''|.|.|''|
      |''|.| |''| | |''|    |''|    |''|    |''|   |''| |.|''|
      |''|.|.|''| | |''|    |''|    |''|    |''| _,|''|.|.|''|
      |''|.| |''|.| |''|    |''|    |''|    |''|/ .|''| |.|''|
      |''|.|.|''| |_|''|`.__|''|,--'|''|``-.|''|   |''|.|.|''|
      |''|.| |''| |.|''| |  |''|  __|''|   ||''|.  |''| |.|''|
      |''|.|.|''| | |''| |  |''| |  |''|   ||''|   |''|.|.|''|
      |''|.| |''|.| |''| |  |''| |  |''|   ||''|  .|''| |.|''|
      |''|.|.|''| | |''| |__|''|_|__|''|___||''|   |''|.|.|''|
      |''|_|_|__| |.|''|'   |''|    |''|    |''|-._|''| |.|''|
      |'/  )| | ||  |''|    |''|    |''|    |''|   |''|'|.|''|
    .-'|`-' | | ||--''''----''''----''''----''''---''''---''''-.
  .'---|| | | |,''--.,-------------------.----------------------'.
 '-----|| | | /  - - - - - - - - ,---. -  \-----------------------'
       || | | : _ _,---._ _ _ _ _`._.'_ _ :                     SSt
       ||_|_|_\  _ `---' _ _ _ ,._ _ _ _  /
               `--------------'--`-------'
''')

# Game: Escape Thriller Bark!
print("Welcome to Thriller Bark!")
print("Your mission is to find your shadows before Gecko Moria takes you.")

direction = input("Which way would you like to go? Type  right or left\n")
if direction == "right" or direction == "Right":
    print("The zombies took you, you won't become the king of the pirates.")
elif direction == "left" or "Left":
    action = input("Choose to jump or swim?\n")
    if action == "swim" or action == "Swim":
        print("Your devil fruit powers failed you, you won't become the king of the pirates.")
    elif action == "jump" or action == "Jump":
        boss = input("Who will you fight? Gecko Moria, Dr. Hogback, or Oars?\n")
        if boss == "Dr. Hogback":
            print("You took back your shadows and escaped!")
        elif boss == "Gecko Moria" or "Oars":
            print("You weren't strong enough to become the king of the pirates.")

# Alternatively, one may use ".lower()" at the end of the input statement
# to make any choice that the user writes become lower case, which eliminates
# the necessity for writing the 'or' statement.
