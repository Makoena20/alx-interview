#!/usr/bin/python3
"""
Module for validating UTF-8 encoding.
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    :param data: List of integers, each representing a byte of data
    :return: True if data is a valid UTF-8 encoding, else return False
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks for checking most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Mask to get only the 8 least significant bits
        byte = num & 0xFF

        if n_bytes == 0:
            # Count the number of leading 1's in the first byte
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask = mask >> 1

            # If n_bytes is 0, it's a 1-byte character
            if n_bytes == 0:
                continue

            # UTF-8 characters can only be 1 to 4 bytes long
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check that the byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes remaining to check
        n_bytes -= 1

    # If we've checked all bytes correctly, n_bytes should be 0
    return n_bytes == 0

