#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Function Description:
    This function computes the factorial of a given non-negative integer `n`. 
    The factorial of a number is the product of all positive integers less than or 
    equal to that number. By definition, the factorial of 0 is 1.

    Parameters:
    - n (int): The non-negative integer whose factorial is to be calculated.

    Returns:
    - int: The factorial of the given integer `n`.
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)