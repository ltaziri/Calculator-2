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
        if tokens[0] == "q":
            break
        elif tokens[0] == "+":
            addition = add(int(tokens[1]), int(tokens[2]))
            print addition


          

calculator()

