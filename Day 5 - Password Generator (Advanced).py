        #Lists of characters to choose from for your password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Choose the number of characters you would like
    # for your password, for each character type.

import random
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

    # Make a random choice of characters from that type,
    # equal to the input from the first step and repeat for
    # other types. Then, create a list for storing this data.

password = [] # The list
for characters in range(0, nr_letters):
    password.append(random.choice(letters))
for characters in range(0, nr_numbers):
    password.append(random.choice(numbers))
for characters in range(0, nr_symbols):
    password.append(random.choice(symbols))

random.shuffle(password) #Shuffle the list

    # Alt 1: Join Function
final_password = "".join(password)
print(f"Your password is {final_password}")

    # Alt 2: Classic
final_password = ""
for char in password:
    final_password += char
print(f"Your password is {final_password}")