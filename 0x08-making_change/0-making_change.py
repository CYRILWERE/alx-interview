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
    
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total == 0:
            break
        count += total // coin
        total %= coin
    
    if total != 0:
        return -1
    return count

