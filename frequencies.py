"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
from collections import Counter

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
    # word_count= Counter(stringItems)
    # frequency = dict(word_count)
    #     if str(item) in frequency:
    #         frequency[str(item)] += 1
    #     else:
    #         frequency[str(item)] = 1
    print(frequency)
