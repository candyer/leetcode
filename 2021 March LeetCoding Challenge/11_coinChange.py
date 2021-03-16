# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3668/


# Coin Change


# You are given coins of different denominations and a total amount of money amount. 
# Write a function to compute the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0

# Example 4:
# Input: coins = [1], amount = 1
# Output: 1

# Example 5:
# Input: coins = [1], amount = 2
# Output: 2
 

# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4

from typing import List
def coinChange(coins: List[int], amount: int) -> int:
    dp = [-1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for val in coins:
            if val <= i:
                if dp[i - val] != -1 and (dp[i] > dp[i - val] or dp[i] == -1):
                    dp[i] = dp[i - val] + 1
    return dp[amount]


assert(coinChange([3, 4], 9) == 3)
assert(coinChange([1,2,5], 11) == 3)
assert(coinChange([2], 3) == -1)
assert(coinChange([1], 0) == 0)
assert(coinChange([1], 1) == 1)
assert(coinChange([1], 2) == 2)



