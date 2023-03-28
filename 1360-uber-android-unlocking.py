"""
Problem #1360

This problem was asked by Uber.

One way to unlock an Android phone is through a pattern of swipes across a 1-9 keypad.

For a pattern to be valid, it must satisfy the following:

All of its keys must be distinct.
It must not connect two keys by jumping over a third key, unless that key has already been used.
For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.

Find the total number of valid unlock patterns of length N, where 1 <= N <= 9.
"""

def count_valid_patterns(pattern_length: int) -> int:
    """
    Counts the number of valid patterns that can be generated given a specific pattern length.

    A valid pattern is defined as a sequence of digits that satisfies the following conditions:
    - Each digit in the pattern is unique.
    - Two adjacent digits in the pattern must be connected either horizontally, vertically, or diagonally on a phone keypad.
    - A digit can only be used once in a pattern.

    Args:
    - pattern_length (int): The length of the pattern to be generated.

    Returns:
    - int: The number of valid patterns that can be generated.
    """
    
    # Precompute the skip matrix.
    skip_matrix = [[0] * 10 for _ in range(10)]
    skip_matrix[1][3] = skip_matrix[3][1] = 2
    skip_matrix[1][7] = skip_matrix[7][1] = 4
    skip_matrix[3][9] = skip_matrix[9][3] = 6
    skip_matrix[7][9] = skip_matrix[9][7] = 8
    skip_matrix[2][8] = skip_matrix[8][2] = skip_matrix[4][6] = skip_matrix[6][4] = skip_matrix[1][9] = skip_matrix[9][1] = skip_matrix[3][7] = skip_matrix[7][3] = 5

    # Initialize memoization dictionary with base case of patterns of length 1.
    memo = {(1, i): 1 for i in range(1, 10)}

    def count_patterns_helper(length: int, last_num: int, used: set) -> int:
        """
        Counts the number of valid patterns of a specific length that end with a specific number.

        A valid pattern is defined as a sequence of digits that satisfies the following conditions:
        - Each digit in the pattern is unique.
        - Two adjacent digits in the pattern must be connected either horizontally, vertically, or diagonally on a phone keypad.
        - A digit can only be used once in a pattern.

        Args:
        - length (int): The current length of the pattern.
        - last_num (int): The last number used in the pattern.
        - used (set): A set of the numbers used in the pattern.

        Returns:
        - int: The number of valid patterns that can be generated.
        """
        if (length, last_num) in memo:
            return memo[(length, last_num)]

        num_patterns = 0
        for next_num in range(1, 10):
            # Check if next_num is available and connected to last_num.
            if next_num not in used and (skip_matrix[last_num][next_num] == 0 or ((skip_matrix[last_num][next_num] + 1) // 2 in used and skip_matrix[last_num][next_num] % 2 == 0)):
                used.add(next_num)
                num_patterns += count_patterns_helper(length + 1, next_num, used)
                used.remove(next_num)

        memo[(length, last_num)] = num_patterns
        return num_patterns

    # Compute the number of valid patterns of length pattern_length.
    num_patterns = 0
    for i in range(1, 10):
        used = set([i])
        num_patterns += count_patterns_helper(1, i, used)

    # Return the total number of valid patterns.
    return num_patterns

