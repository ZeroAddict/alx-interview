#!/usr/bin/python3
"""
function canUnlockAll checks if boxes stay locked or unlocked
"""


def canUnlockAll(boxes):
    """
    Determines whether a type list(list) locked boxes can all be unlocked
    based on keys that can be accessed.
    """
    # Check if list is empty
    if len(boxes) == 0:
        return False

    # Check if input is a list
    if (type(boxes)) is not list:
        return False

    for x in range(1, len(boxes) - 1):
        checked_boxes = False
        for idx in range(len(boxes)):
            checked_boxes = x in boxes[idx] and x != idx
            if checked_boxes:
                break
        if checked_boxes is False:
            return checked_boxes
    return True
