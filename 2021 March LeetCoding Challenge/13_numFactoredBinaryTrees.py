# https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3670/

# Binary Trees With Factors


# Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.
# We make a binary tree using these integers, and each number may be used for any number of times. 
# Each non-leaf node's value should be equal to the product of the values of its children.
# Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

# Example 1:
# Input: arr = [2,4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]

# Example 2:
# Input: arr = [2,4,5,10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
 

# Constraints:
# 1 <= arr.length <= 1000
# 2 <= arr[i] <= 10^9

from typing import List

def numFactoredBinaryTrees(arr: List[int]) -> int:
    mod = 10 ** 9 + 7
    n = len(arr)
    arr.sort()
    dp = [1] * n
    index = {num: i for i, num in enumerate(arr)}
    for i, num in enumerate(arr):
        for j in range(i):
            if num % arr[j] == 0:
                node = num // arr[j]
                if node in index:
                    dp[i] += dp[j] * dp[index[node]]
                    dp[i] %= mod
    return sum(dp) % mod

# print(numFactoredBinaryTrees([2,4]))
# print(numFactoredBinaryTrees([2,4,5,10]))
print(numFactoredBinaryTrees([2,4,5,10,40]))

