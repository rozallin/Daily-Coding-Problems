"""
This problem was asked by Affirm.

Given a array of numbers representing the stock prices of a company in chronological
order, write a function that calculates the maximum profit you could have made from
buying and selling that stock. You're also given a number fee that represents a
transaction fee for each buy and sell transaction.
You must buy before you can sell the stock, but you can make as many transactions as
you like.
For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9, since you
could buy the stock at $1, and sell at $8, and then buy it at $4 and sell it at $10.
Since we did two transactions, there is a $4 fee, so we have 7 + 6 = 13 profit minus $4
of fees.

Time complexity of solution: O(n)
Space complexity of solution: O(1)
"""

from typing import List

def get_max_profit(prices: List[int], fee: int) -> int:
"""
Given a list of prices and a transaction fee, returns the maximum profit that can be made by buying and selling
the stock with the given prices. Assumes that prices is a list of integers and fee is a positive integer.

Args:
    prices (List[int]): A list of integers representing the prices of the stock on each day.
    fee (int): An integer representing the transaction fee.

Returns:
    int: The maximum profit that can be made by buying and selling the stock with the given prices.
"""
    # Check that input is valid
    if not all(isinstance(price, int) for price in prices):
        raise ValueError("Prices list must contain only integers")
    if fee <= 0:
        raise ValueError("Fee must be a positive integer")

    n = len(prices)
    if n < 2:
        return 0

    # Initialize variables
    max_profit_buy = -prices[0] - fee  # The maximum profit if the stock is bought on the first day
    max_profit_sell = 0  # The maximum profit if the stock is not held on the first day

    # Iterate over the prices
    for i in range(1, n):
        # Temporarily hold the maximum profit if the stock is bought on the previous day
        temp = max_profit_buy
        # Update the maximum profit if the stock is bought today
        max_profit_buy = max(max_profit_buy, max_profit_sell - prices[i] - fee)
        # Update the maximum profit if the stock is not held today
        max_profit_sell = max(max_profit_sell, temp + prices[i])

    return max_profit_sell
