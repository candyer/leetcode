
# https://leetcode.com/problems/coin-change/description/

# You are given coins of different denominations and a total amount of money amount. 
# Write a function to compute the fewest number of coins that you need to make up 
# that amount. If that amount of money cannot be made up by any combination of the 
# coins, return -1.

# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)

# Example 2:
# coins = [2], amount = 3
# return -1.

# Note:
# You may assume that you have an infinite number of each kind of coin.

def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    dp = [-1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for val in coins:
            if val <= i:
                if dp[i - val] != -1 and (dp[i] > dp[i - val] or dp[i] == -1):
                    dp[i] = dp[i - val] + 1
    return dp[amount]

print coinChange([2,3,5], 12) #3
print coinChange([2,4,6], 11) #-1
print coinChange([5,3,1], 11) #3
print coinChange([7,2,3,6], 13) #2


