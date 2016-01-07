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

        x = len(tokens)
        if x > 1:
            i = x - 1
            while i > 0:      # is there a better way?
                tokens[i] = int(tokens[i])
                i = i - 1

            if tokens[0] == "+":
                addition = add(tokens[1], tokens[2])
                print addition
            elif tokens[0] == "-":
                subtraction = subtract(tokens[1], tokens[2])
                print subtraction
            elif tokens[0] == "*":
                multiplication = multiply(tokens[1], tokens[2])
                print multiplication
            elif tokens[0] == "/":
                division = divide(tokens[1], tokens[2])
                print division
            elif tokens[0] == "square":
                num_square = square(tokens[1])
                print num_square
            elif tokens[0] == "cube":
                num_cube = cube(tokens[1])
                print num_cube
            elif tokens[0] == "pow":
                num_power = power(tokens[1], tokens[2])
                print num_power
            elif tokens[0] == "mod":
                num_mod = mod(tokens[1], tokens[2])
                print num_mod
        else:
            if tokens[0] == "q":
                break
            else:
                print "This is not a valid entry"


calculator()

