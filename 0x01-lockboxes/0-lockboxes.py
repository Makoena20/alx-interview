#!/usr/bin/python3
"""
This module contains the canUnlockAll function which
determines if all boxes in a list of boxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Parameters:
        boxes (list of list of int): A list of lists where each list contains keys to other boxes.
    
    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop(0)
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
