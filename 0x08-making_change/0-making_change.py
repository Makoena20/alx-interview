#!/usr/bin/python3
"""
Change comes from within
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (list): a list of the values of the coins in your possession
    total (int): the total amount to reach using the coins

    Returns:
    int: the fewest number of coins needed to meet the total
         or -1 if the total cannot be met
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    count = 0
    for coin in coins:
        if total >= coin:
            count += total // coin  # Use as many coins of this denomination as possible
            total = total % coin  # Reduce the total by the amount covered by these coins
        
        if total == 0:
            return count  # Return the number of coins if total is met

    return -1  # If the loop completes and total is not 0, return -1

