#!/usr/bin/python3
"""
This module contains a function to calculate the minimum operations needed
to achieve exactly n 'H' characters in a file starting with a single 'H'.
"""

def minOperations(n):
    """
    Calculate the minimum number of operations to result in exactly n 'H' characters.
    
    Parameters:
    n (int): The target number of 'H' characters
    
    Returns:
    int: The minimum number of operations required, or 0 if n is impossible to achieve
    """
    if n < 2:
        return 0
    
    operations = 0
    factor = 2
    
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations

