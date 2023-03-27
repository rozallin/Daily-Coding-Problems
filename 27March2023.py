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
    n = len(prices)
    if n < 2:
        return 0

    # initialize the variables
    hold = -prices[0] - fee
    not_hold = 0

    # iterate over the prices
    for i in range(1, n):
        temp = hold
        hold = max(hold, not_hold - prices[i] - fee)
        not_hold = max(not_hold, temp + prices[i])

    return not_hold


if __name__ == "__main__":
    print(get_max_profit([1, 3, 2, 8, 4, 10], 2))
    print(get_max_profit([1, 3, 2, 1, 4, 10], 2))
