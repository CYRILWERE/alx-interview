#!/usr/bin/python3
"""
Module to determine if all lockboxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Args:
    boxes (list of list of int): a list where each element is a list of keys contained in a box.
    
    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = boxes[0]
    
    while keys:
        new_keys = []
        for key in keys:
            if key < n and not opened[key]:
                opened[key] = True
                new_keys.extend(boxes[key])
        keys = new_keys
    
    return all(opened)

