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
    
    # Initialize dp array to total+1, which is effectively "infinity"
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make 0 amount
    
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[total] if dp[total] <= total else -1

