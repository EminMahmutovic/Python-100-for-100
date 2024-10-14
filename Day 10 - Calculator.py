                                            ### Calculator ###
                                # This program creates a simple calculator using
                                # knowledge of loops, dictionaries and functions.




# Operators                                 # Define operators for addition, subtraction
def add(n1, n2):                            # multiplication and division.
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Dictionary with operators
operations = {                              # Add them to a dictionary to be able to use them
    "+": add,                               # more fluidly later.
    "-": subtract,
    "*": multiply,
    "/": divide
}

######################

from art import logo #ASCII Art
print(logo)

def calculator():                                                                   # The logic for the calculator is as follows:
    should_continue = True                                                          # Ask the user for a starting number, let them
    firstnumber = float(input("What's the first number?"))                          # pick an operation from the dictionary "Operations",
                                                                                    # choose another number, perform the calculation.
    while should_continue:                                                          # Additionally, we want to know if they want to
        for symbol in operations:                                                   # continue using the same result for new calc.
            print(symbol)                                                           # or start over, which is why a while loop is used.
        choice_of_operation = input("Pick an operation")                            # The main problem here is to ask for the initial
        nexttnumber = float(input("What's the next number?"))                       # number again without rewriting it, and simultaneously,
        result = operations[choice_of_operation](firstnumber, nexttnumber)          # if the choice is no, how we should break out of the loop
        print(f"{firstnumber} {choice_of_operation} {nexttnumber} = {result}")      # and remove previous results.

        choice = input(f"Type 'y' to continue calculating with {result},"           # For this, we implement recursion into the while loop.
          f" or type 'n' to start a new calculation").lower()                       # Define a function called "Calculator" that contains the loop.
                                                                                    # If the choice is no, we end the loop. However, we call the
        if choice == "y":                                                           # function within itself, which will make it start from the
            firstnumber = result                                                    # beginning instead of the while loop. Also, we add some
        else:                                                                       # empty lines to represent the "erasure" of previous results.
            should_continue = False
            print("\n" * 20)
            calculator()
calculator()


