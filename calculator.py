"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

def calculator():
    while True:
        data = raw_input()
        tokens = data.split(" ")
        
                            
        if len(tokens)>1:
            int_tokens = [tokens[0]]
            for token in tokens[1: ]:
                int_tokens.append(int(token))
            print int_tokens
            if int_tokens[0] == "+":
                addition = add(int_tokens[1], int_tokens[2])
                print addition
            elif int_tokens[0] == "-":
                subtraction = subtract(int_tokens[1], int_tokens[2])
                print subtraction
            elif int_tokens[0] == "*":
                multiplication = multiply(int_tokens[1], int_tokens[2])
                print multiplication
            elif int_tokens[0] == "/":
                division = divide(int_tokens[1], int_tokens[2])
                print division
            elif int_tokens[0] == "square":
                num_square = square(int_tokens[1])
                print num_square
            elif int_tokens[0] == "cube":
                num_cube = cube(int_tokens[1])
                print num_cube
            elif int_tokens[0] == "pow":
                num_power = power(int_tokens[1], int_tokens[2])
                print num_power
            elif int_tokens[0] == "mod":
                num_mod = mod(int_tokens[1], int_tokens[2])
                print num_mod
            else:
                print "That is not a valid entry!"
        else:
            if tokens[0] == "q":
                break
            else:
                print "This is not a valid entry"

calculator()
 # x = len(tokens)
        # if x > 1:
        #     i = x - 1
        #     while i > 0:      # is there a better way?
        #         tokens[i] = int(tokens[i])
        #         i = i - 1
