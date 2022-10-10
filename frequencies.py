"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequency = {}

    for item in items:
        if str(item) in frequency:
            frequency[str(item)] += 1
        else:
            frequency[str(item)] = 1
    print(frequency)
