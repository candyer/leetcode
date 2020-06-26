# https://leetcode.com/explore/featured/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3370/

# Unique Binary Search Trees

# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

# Example:

# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


from typing import List
def numTrees(n: int) -> int:
	if n == 0: 
		return 1
	dp = [0] * (n + 1)
	dp[0] = dp[1] = 1
	for i in range(2, n + 1):
		for j in range(i):
			dp[i] += dp[j] * dp[i - j - 1]
	return dp[-1]

assert(numTrees(4) == 14)
assert(numTrees(10) == 16796)







