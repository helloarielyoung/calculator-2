"""Math functions for calculator."""


def add(num_list):
    """Return the sum of the two input integers."""

    for num in num_list:
        num += num

    return num


def subtract(num_list):
    """Return the second number subtracted from the first."""
    print num_list

    for num in num_list[::-1]:
        print "printing num" + str(num)
        num = num - num
    return num


def multiply(num1, num2):
    """Multiply the two inputs together."""

    return num1 * num2


def divide(num1, num2):
    """Divide the first input by the second, returning a floating point."""

    # Need to turn at least one argument to float for division to
    # not be integer division

    return float(num1) / num2


def square(num1):
    """Return the square of the input."""

    # Needs only one argument

    return num1 * num1


def cube(num1):
    """Return the cube of the input."""

    # Needs only one argument

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2
