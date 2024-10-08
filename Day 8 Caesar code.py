                                                    ### Creating a Caesar code ###

                                        # The purpose is to use a list with an alphabet, choose a word to
                                        # encode or decode using simple shifting of indices.
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):                  # Our function uses 3 parameters:
    output_text = ""                                                        # 1. Original_text: word to encode/decode
                                                                            # 2. Shift_amount: int. of shift in characters
                                                                            # 3. encode_or_decode: the decision
                                                                            # In this step, we define the function, later on,
                                                                            # the input for these are written in the while loop.

    if encode_or_decode == "decode":                                        # The only difference between encoding and decoding is
        shift_amount *= -1                                                  # a positive or negative shift.

    for letter in original_text:                                            # The function checks every letter in the word, if there is
        if letter not in original_text:                                     # another type of symbol, it doesn't count it towards the
            output_text += letter                                           # encryption/decryption, but adds it to the final word instead.
        else:                                                               # Otherwise, we create the shifted_position as an index including
            shifted_position = alphabet.index(letter) + shift_amount        # the shift, and use this to create the output_text. Also, to ensure
            shifted_position %= len(alphabet)                               # that we don't go outside the list range, we use a modulo operation.
            output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue = True                                                                      # Variable for testing if we should continue running the function

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()      # After defining the function, this is where our console output begins.
    text = input("Type your message:\n").lower()                                            # The user gets to choose the text, shift, and direction. Then use this
    shift = int(input("Type the shift number:\n"))                                          # input in the caesar function.

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' to go again. Otherwise, type 'no'\n").lower()               # Decision to continue or halt.
    if restart == "no":
        should_continue = False
        print("Goodbye")



