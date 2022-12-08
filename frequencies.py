"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequency = {}
    stringItems = []
    for item in items:
        stringItems.append(str(item))

    for item in stringItems:
        if item not in frequency:
            frequency[item] = 1
        else:
            frequency[item] += 1
    return frequency
