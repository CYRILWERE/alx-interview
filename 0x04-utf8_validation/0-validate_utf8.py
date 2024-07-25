#!/usr/bin/python3
"""
Module to validate if a given data set represents a valid UTF-8 encoding
"""

def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    
    Args:
    data (list of int): The data set to validate, represented by a list of integers.
    
    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    n_bytes = 0

    for num in data:
        # Get the binary representation. We only need the least significant 8 bits
        bin_rep = format(num, '#010b')[-8:]

        if n_bytes == 0:
            # Count the number of leading 1's in the first byte
            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1

            # 1-byte character
            if n_bytes == 0:
                continue

            # UTF-8 characters can be 1 to 4 bytes long
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False

        n_bytes -= 1

    return n_bytes == 0

