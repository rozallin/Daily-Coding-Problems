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


def validate_input(prices: List[int], transaction_fee: int) -> None:
    """
    Validates the input for the get_max_profit function, raising an error if the input is invalid.

    Args:
        prices (List[int]): A list of integers representing the stock prices in chronological order.
        transaction_fee (int): An integer representing the transaction fee for each buy and sell transaction.

    Raises:
        AssertionError: If prices is not a list of integers or if transaction_fee is negative.
    """
    assert isinstance(prices, list), "prices must be a list of integers"
    assert all(isinstance(price, int) for price in prices), "prices must be a list of integers"
    assert transaction_fee >= 0, "transaction_fee must be a non-negative integer"


def get_max_profit(prices: List[int], transaction_fee: int) -> int:
    """
    Calculates the maximum profit that can be made from buying and selling a stock with transaction fees.

    Args:
        prices (List[int]): A list of integers representing the stock prices in chronological order.
        transaction_fee (int): An integer representing the transaction fee for each buy and sell transaction.

    Returns:
        int: The maximum profit that can be made from buying and selling the stock.

    Raises:
        AssertionError: If prices is not a list of integers or if transaction_fee is negative.
    """
    validate_input(prices, transaction_fee)

    if len(prices) < 2:
        return 0

    # Initialize the maximum profit with and without the stock
    max_profit_with_stock, max_profit_without_stock = -prices[0] - transaction_fee, 0

    # Loop through the prices starting from the second one
    for price in prices[1:]:
        # Update the maximum profit with and without the stock
        max_profit_with_stock = max(max_profit_with_stock, max_profit_without_stock - price - transaction_fee)
        max_profit_without_stock = max(max_profit_without_stock, max_profit_with_stock + price)

    return max_profit_without_stock

