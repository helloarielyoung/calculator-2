"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

#declare variable for our list of numbers
num_list = []

# Your code goes here
def my_calculator():
    """This function performs a mathmatical operation
        chosen based on user input

        Based on the input from the user, it calls out to
        the math functions in arithmetic.py
    """

    calculator_on = True

    while calculator_on:
        #get input from the user
        input_string = raw_input()

        #break user input into a list
        tokens = input_string.split(" ")

        #first list item is the mathmatical operator
        operator = tokens[0]

        #iterate through tokens and turn list into integers
        for number in tokens[1:]:
            num_list.append(int(number)) #Q: what if they submit a decimal?

        # Here we start doing the math
        if operator == "+":
            print add(num_list)

        elif operator == "-":
            print subtract(num_list)

        elif operator == "*":
            print multiply(num_list)

        elif operator == "/":   # when adding error checking, check for division by 0
            print divide(float(num1), num2)

        elif operator == "square":  # consider adding 'or **'
            print square(num1)

        elif operator == "cube":
            print cube(num1)

        elif operator == "pow":  #consider adding 'or ^'?
            print power(num1, num2)

        elif operator == "mod":
            print mod(num1, num2)

        elif operator == 'q':
            calculator_on = False

            #add else for invalid input


my_calculator()
