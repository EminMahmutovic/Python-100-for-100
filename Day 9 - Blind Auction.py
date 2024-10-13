                                                            ### Blind Auction ###
                                        # The purpose is to create an auction where the users don't know
                                        # eachothers bids. 

import art #ASCII art
print(art.logo)
                                                                        # The auction program starts from line 23. However,
                                                                        # we first need to create a function that compares
                                                                        # bids to later use in the upcoming while loop.

def find_highest_bidder(bidding_dictionary):                            # Create a function for finding the highest bidder
    winner = ""                                                         # Create a parameter called "bidding_dictionary" and variable
    highest_bid = 0                                                     # "bidder" for a loop that compares the "bid_amount" with "price"
    for bidder in bidding_dictionary:                                   # and then chooses who the highest bidder is.
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

bids = {}                                                               # Create a dictionary whose keys are the names of the bidders
                                                                        # and price are the values, seen in line 29.
continue_bidding = True                                                 # Condition for checking for other bidders in the coming
                                                                        # while loop.

while continue_bidding:                                                                     # Ask for name and price. Add the key & value pairs
    name = input("What is your name?")                                                      # to the dictionary, and ask if there are more bidders?
    price = int(input("What is your bid?"))                                                 # If no, we set the condition in line 23 as false, and perform
    bids[name] = price                                                                      # the find_highest_bidder function, using "bids" dictionary
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()     # as argument for the "bidding_dictionary" parameter.
    if other_bidders == "no":                                                               # If instead "yes", we print some empty lines to represent
        continue_bidding = False                                                            # the "erasure" of other data (i.e., assuming the participants
        find_highest_bidder(bids)                                                           # can't scroll, adding extra lines will hide everybody's
    elif other_bidders == "yes":                                                            # results from each other), making it a blind auction.
        print("\n" * 20)
