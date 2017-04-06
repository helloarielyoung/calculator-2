"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here
def my_calculator():
    """This function performs a mathmatical operation
        chosen based on user input

        Based on the input from the user, it calls out to
        the math functions in arithmetic.py
    """

    calculator_on = True

    while calculator_on:

        input_string = raw_input()

        tokens = input_string.split(" ")

        operator = tokens[0]

        if len(tokens) > 1:
            num1 = float(tokens[1])
            if len(tokens) > 2:
                num2 = float(tokens[2])

        # Here we start doing the math
        if operator == "+":
            print add(num1, num2)

        elif operator == "-":
            print subtract(num1, num2)

        elif operator == "*":
            print multiply(num1, num2)

        elif operator == "/":   # when adding error checking, check for division by 0
            print divide(num1, num2)

        elif operator == "square":  # consider adding 'or **'
            print square(num1)

        elif operator == 'q':
            calculator_on = False


my_calculator()
