"""
# -----------------------------
# File : q1.py
# Created :  28/09/2021
# Author : Rohit Mishra
# Version : v1.0.0
# Py Version : 2021.2.2
# Licensing : (C) 2021 Rohit Mishra, LYIT
#              Available under GNU Public License (GPL)
# Description : Number Guessing Game
# -----------------------------
"""



if __name__ == '__main__':
    main_number = 6
    guess_is_wrong = True
    input_is_a_number = True

    while input_is_a_number and guess_is_wrong:  # this condition must evaluate to True to continue.

        # take a new value.
        # always returns value in string format. That is why we will type cast the value below.

        input_value = input("Enter a new number to guess, or type No to quit\n")
        print(f"User input is = {input_value}")

        # find loop fail conditions
        if input_value == "No":
            input_is_a_number = False
        else:
            if int(input_value) == main_number:
                print("You guessed it right!!")
