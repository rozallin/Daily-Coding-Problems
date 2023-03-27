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
Time complexity of solution: O(N)
Space complexity of solution: O(1)
"""

from typing import Sequence


def get_max_profit(prices: Sequence[int], transaction_fee: int) -> int:
    """
    Calculates the maximum profit that can be made from buying and selling a stock with transaction fees.
    The function takes in a sequence of integers representing the stock prices in chronological order,
    as well as an integer representing the transaction fee for each buy and sell transaction. It then
    calculates the maximum profit that can be made from buying and selling the stock with the given transaction
    fees, taking into account that multiple transactions can be made.
    Args:
        prices: A sequence of integers representing the stock prices in chronological order.
        transaction_fee: An integer representing the transaction fee for each buy and sell transaction.
    Returns:
        The maximum profit that can be made from buying and selling the stock.
    Raises:
        ValueError: If prices is an empty sequence or transaction_fee is negative.
        TypeError: If prices contains non-integer values or transaction_fee is not an integer.
    """
    # Validate input
    assert prices, "prices cannot be empty"
    assert all(isinstance(price, int) and price >= 0 for price in prices), "prices must contain only non-negative integers"
    assert isinstance(transaction_fee, int) and transaction_fee >= 0, "transaction_fee must be a non-negative integer"

    # Handle edge case where there are less than 2 prices
    if len(prices) < 2:
        return 0

    # Initialize the maximum profit with and without the stock
    max_profit_with_stock = float('-inf') # The maximum profit we can have if we own the stock
    max_profit_without_stock = 0 # The maximum profit we can have if we don't own the stock

    # Loop through the prices starting from the second one
    for i in range(1, len(prices)):
        # Update the maximum profit with and without the stock
        # The maximum profit with the stock is either the previous maximum profit with the stock or the maximum profit without the stock minus the current price and transaction fee
        max_profit_with_stock = max(max_profit_with_stock, max_profit_without_stock - prices[i] - transaction_fee)
        # The maximum profit without the stock is either the previous maximum profit without the stock or the maximum profit with the stock plus the difference in price since the previous day
        max_profit_without_stock = max(max_profit_without_stock, max_profit_with_stock + prices[i] - prices[i-1])

    # Return the maximum profit without the stock, since that is the maximum profit we can achieve after all transactions are made
    return max_profit_without_stock
