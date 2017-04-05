"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

# tokens = input_string.split(" ")   # => ["pow", "3", "5"]

#while True is going to be here
input_string = raw_input()

tokens = input_string.split(" ")

# Get the operator and the numbers from the user's input

operator = tokens[0]
num1 = float(tokens[1])
num2 = float(tokens[2])


def my_calculator(operator, num1, num2 = None):
    """This function performs a mathmatical operation
        chosen based on user input

        Based on the input from the user, it calls out to
        the math functions in arithmetic.py
    """

    #for testing:
    #print add(num1, num2)

    if operator == "+":
        print add(num1, num2)
