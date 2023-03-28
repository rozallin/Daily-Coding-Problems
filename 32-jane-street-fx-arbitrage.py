"""
This problem was asked by Jane Street.

Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: 
that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up 
with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.

Space complexity: O(N^2)
Time complexity: O(N^3)
"""

from math import log

def has_arbitrage(exchange_rates):
    """
    Determine whether there is a possible arbitrage using a table of currency exchange rates.

    Args:
        exchange_rates (list of list of float): A 2D array representing currency exchange rates.
            exchange_rates[i][j] is the exchange rate from currency i to currency j.

    Returns:
        bool: True if there is an arbitrage, False otherwise.

    Raises:
        ValueError: If the input is not a valid 2D array of floats.

    Examples:
        >>> has_arbitrage([[1.0, 2.0], [0.5, 1.0]])
        False
        >>> has_arbitrage([[1.0, 0.5], [2.0, 1.0]])
        True
    """
    # Validate input
    if not isinstance(exchange_rates, list) or not all(isinstance(row, list) for row in exchange_rates):
        raise ValueError("Input must be a list of lists.")
    if not all(isinstance(rate, float) for row in exchange_rates for rate in row):
        raise ValueError("All elements of the input must be floats.")

    # Convert exchange rates to negative logarithms so that we can add them instead of multiplying
    neg_log_rates = ([-log(rate) for rate in row] for row in exchange_rates)

    # Run the Bellman-Ford algorithm to detect negative weight cycles
    n = len(exchange_rates)
    dist = [float('inf')] * n
    dist[0] = 0
    for _ in range(n - 1):
        for source, target, weight in get_edges(neg_log_rates):
            if dist[source] + weight < dist[target]:
                dist[target] = dist[source] + weight
    if any(dist[source] + weight < dist[target] for source, target, weight in get_edges(neg_log_rates)):
        return True
    return False

def get_edges(graph):
    """
    Helper function that yields edges of a graph represented by a 2D array.

    Args:
        graph (list of list of float): A 2D array representing a graph.
            graph[i][j] is the weight of the edge from vertex i to vertex j.

    Yields:
        tuple: A tuple of three values representing an edge in the graph.
            The first two values are the source and target vertices, respectively.
            The third value is the weight of the edge.

    Raises:
        ValueError: If the input is not a valid 2D array of floats.

    Examples:
        >>> list(get_edges([[1.0, 2.0], [0.5, 1.0]]))
        [(0, 1, 2.0), (1, 0, 0.5)]
        >>> list(get_edges([[1.0, 0.5], [2.0, 1.0]]))
        [(0, 1, 0.5), (1, 0, 2.0)]
    """
    # Validate input
    if not isinstance(graph, list) or not all(isinstance(row, list) for row in graph):
        raise ValueError("Input must be a list of lists.")
    if not all(isinstance(weight, float) for row in graph for weight in row):
        raise ValueError("All elements of the input must be floats.")

    n = len(graph)
    for source in range(n):
        for target in range(source + 1, n):
            weight = graph[source][target]
            if weight != 0:
