"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def calculator(data):

    while True:
        tokens = data.split(" ")
        if tokens[0] == "q":
            break
        elif tokens[0] == "+":
            