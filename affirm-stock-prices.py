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

def validate_inputs(prices_list, transaction_fee):
    """
    Validate inputs to ensure they meet requirements.
    :param prices_list: (list) list of prices
    :param transaction_fee: (int) fee amount
    :raises TypeError: if prices_list is not a list or transaction_fee is not an integer
    :raises ValueError: if prices_list contains a non-integer element
    """
    if not isinstance(prices_list, list):
        raise TypeError(f"Invalid type for argument 'prices_list': expected list, but got {type(prices_list).__name__}")

    for i, price in enumerate(prices_list):
        if not isinstance(price, int):
            raise ValueError(f"Invalid type for element {i} of argument 'prices_list': expected int, but got {type(price).__name__}")

    if not isinstance(transaction_fee, int):
        raise TypeError(f"Invalid type for argument 'transaction_fee': expected int, but got {type(transaction_fee).__name__}")

def calculate_max_profit(prices_list, transaction_fee):
    """
    Calculate the maximum profit that can be made from buying and selling a stock.
    :param prices_list: (list) list of prices
    :param transaction_fee: (int) fee amount
    :return: (int) maximum profit that can be made
    :raises TypeError: if prices_list is not a list or transaction_fee is not an integer
    :raises ValueError: if prices_list contains a non-integer element
    """
    validate_inputs(prices_list, transaction_fee)
    number_of_prices = len(prices_list)

    if number_of_prices < 2:
        return 0

    max_profit_when_buying, max_profit_when_selling = -prices_list[0], 0

    for i in range(1, number_of_prices):
        # Calculate the maximum profit that can be made from buying at this price
        # and subtracting the transaction_fee.
        potential_buy_profit = max_profit_when_selling - prices_list[i] - transaction_fee

        # Calculate the maximum profit that can be made from selling at this price.
        potential_sell_profit = max_profit_when_buying + prices_list[i]

        # Update the maximum buy profit if the potential buy profit is greater.
        max_profit_when_buying = max(max_profit_when_buying, potential_buy_profit)

        # Update the maximum sell profit if the potential sell profit is greater.
        max_profit_when_selling = max(max_profit_when_selling, potential_sell_profit)

    return max_profit_when_selling
