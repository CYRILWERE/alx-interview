#!/usr/bin/python3
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    :param coins: List of coin denominations.
    :param total: Total amount to achieve using the coins.
    :return: Fewest number of coins needed to achieve the total. If not possible, return -1.
    """
    if total <= 0:
        return 0
    
    # Initialize DP array with a large number (total + 1) since total is the max needed
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1

