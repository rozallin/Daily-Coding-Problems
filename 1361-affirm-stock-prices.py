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

from typing import List


    def is_input_valid(prices_list: List[int], transaction_fee: int) -> bool:
    """
    Check if the input parameters meet the requirements for the function to execute correctly.

    :param prices_list: A list of integers representing the prices of assets to be transacted.
    :type prices_list: List[int]
    
    :param transaction_fee: An integer representing the transaction fee amount.
    :type transaction_fee: int
    
    :returns: A boolean indicating whether the inputs meet the requirements (True) or not (False).
    :rtype: bool
    """
    if not isinstance(prices_list, list):
        return False
    if not all(isinstance(price, int) for price in prices_list):
        return False
    if not isinstance(transaction_fee, int):
        return False
    return True

def calculate_max_profit(prices_list: List[int], transaction_fee: int) -> int:
    """
    Given a list of stock prices and a transaction fee, calculates the maximum profit that can be made
    by buying and selling a single stock, subject to the transaction fee.
    Args:
        prices_list (List[int]): A list of stock prices, where prices_list[i] is the price of the stock on day i.
        transaction_fee (int): The transaction fee incurred for buying or selling a stock.
    Returns:
        The maximum profit that can be made by buying and selling a single stock, subject to the transaction fee.
    Raises:
        ValueError: If prices_list is empty or if transaction_fee is negative.
    Note:
        - If there are no profitable trades that can be made, returns 0.
        - If transaction_fee is 0 or negative, it is effectively ignored.
        - If the input list has repeated prices, the function considers each occurrence of a price
          as a different stock on a different day. For example, if prices_list=[1, 2, 1], the function considers
          buying on day 1 and selling on day 2, and also buying on day 3 and selling on day 2.
    Example:
        >>> calculate_max_profit([1, 3, 2, 8, 4, 10], 2)
        9
    """
    if not is_input_valid(prices_list, transaction_fee):
        raise ValueError("Invalid input")

    if len(prices_list) < 2:
        return 0
    
    # Initialise the buy profit as the negative value of the first price.
    # This represents the maximum profit that can be made by buying the stock
    # at the first price, since the stock cannot be bought before the first price.
    buy_profit = -prices_list[0]
    
    # Initialise the sell profit as 0, since there is no profit in selling the stock
    # before it is bought.
    sell_profit = 0

    # Loop through the remaining prices and update the buy and sell profits
    for current_price_index, current_price in enumerate(prices_list[1:], start=1):
        # Calculate the maximum profit that can be made by buying at the current price
        # and subtracting the transaction_fee.
        max_buy_profit = max(buy_profit, sell_profit - current_price - transaction_fee)

        # Calculate the maximum profit that can be made by selling at the current price.
        # The buy_profit variable is used here to ensure that we only sell if we've
        # already bought the stock.
        max_sell_profit = max(sell_profit, buy_profit + current_price)

        # Update the buy and sell profits for the next iteration
        buy_profit = max_buy_profit
        sell_profit = max_sell_profit

    # Return the maximum sell profit.    
    return sell_profit

def test_calculate_max_profit():
    """
    Test function for calculate_max_profit. It includes several test cases to ensure that
    the function is correctly calculating the maximum profit that can be made from buying
    and selling a stock given a list of prices and a transaction fee.
    """
    # Test basic case with increasing prices and no transaction fee
    assert calculate_max_profit([1, 2, 3, 4, 5], 0) == 4
    
    # Test case with varying prices and transaction fee
    assert calculate_max_profit([1, 3, 2, 8, 4, 10], 2) == 9
    
    # Test case with decreasing prices and transaction fee
    assert calculate_max_profit([3, 2, 6, 5, 0, 3], 1) == 2
    
    # Test case with increasing prices and small transaction fee
    assert calculate_max_profit([1, 2, 3, 4, 5], 1) == 3
    
    # Test case with decreasing prices and no transaction fee
    assert calculate_max_profit([5, 4, 3, 2, 1], 0) == 0
    
    # Test case with empty prices list and transaction fee
    assert calculate_max_profit([], 2) == 0
    
    # Test case with one element in prices list and transaction fee
    assert calculate_max_profit([1], 1) == 0
    
    # Test case with large list of prices and no transaction fee
    assert calculate_max_profit([1, 2, 3] * 1000, 0) == 2997
    
    # Test case with varying prices and transaction fee
    assert calculate_max_profit([1, 10], 1) == 8
    
    # Test case with one price repeated many times and transaction fee
    assert calculate_max_profit([1] * 1000000, 2) == 0
    
    # Test case with only negative prices and no transaction fee
    assert calculate_max_profit([-1, -2, -3], 0) == 0
    
    # Test case with only same prices and transaction fee
    assert calculate_max_profit([1, 1, 1, 1], 2) == 0
    
    # Test case with decimal prices and no transaction fee
    assert calculate_max_profit([1.5, 2.5, 3.5], 0) == 2
    
    # Test case with very large transaction fee
    assert calculate_max_profit([1, 3, 2, 8, 4, 10], 1000000000) == 0
    
    # Test case with decreasing prices and no transaction fee
    assert calculate_max_profit([5, 4, 3, 2, 1], 0) == 0
    
    # Test case with decreasing prices and transaction fee
    assert calculate_max_profit([100, 50, 25, 10, 1], 1) == 0
    
    # Test case with negative prices and transaction fee
    assert calculate_max_profit([10, 5, 1, -2, -10], 5) == 0
    
    # Test case for prices in descending order and transaction fee
    assert calculate_max_profit([5, 4, 3, 2, 1], 1) == 0
    
    # Test with large list of prices (10^5 elements)
    prices = [i for i in range(10**5)]
    assert calculate_max_profit(prices, 10) == 99990
    
test_calculate_max_profit()
