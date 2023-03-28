"""
Problem #1362 [Easy]

This problem was asked by Google.

A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she goes along, 
but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest portion 
of her path that consists of just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four.

Time complexity: O(n)
Space complexity: O(k)
"""

def longest_two_types_path(apples):
    """
    Finds the length of the longest portion of a path consisting of just two types of apple trees.

    Args:
        apples: A list of integers representing the types of apple trees on the path.

    Returns:
        An integer representing the length of the longest portion of the path consisting of just two types of apple trees.
    """

    start = 0   # The start index of the current window
    end = 0     # The end index of the current window
    max_length = 0  # The maximum length of a window with two types of apple trees
    types = set()   # A set containing the types of apple trees in the current window

    while end < len(apples):
        types.add(apples[end])  # Add the current type of apple tree to the set

        # Shrink the window from the left side if there are more than two types of apple trees in the window
        if len(types) > 2:
            while len(types) > 2:
                if apples[start] in types:
                    types.remove(apples[start])
                start += 1

        # Update the maximum length if the current window has only two types of apple trees and is longer than the previous maximum length
        max_length = max(max_length, end - start + 1)
        
        end += 1    # Move the window one step to the right

    return max_length





