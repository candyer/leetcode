# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/

# 1155. Number of Dice Rolls With Target Sum

# You have d dice, and each die has f faces numbered 1, 2, ..., f.

# Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum 
# of the face up numbers equals target.

 
# Example 1:
# Input: d = 1, f = 6, target = 3
# Output: 1
# Explanation: 
# You throw one die with 6 faces.  There is only one way to get a sum of 3.

# Example 2:
# Input: d = 2, f = 6, target = 7
# Output: 6
# Explanation: 
# You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
# 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

# Example 3:
# Input: d = 2, f = 5, target = 10
# Output: 1
# Explanation: 
# You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.

# Example 4:
# Input: d = 1, f = 2, target = 3
# Output: 0
# Explanation: 
# You throw one die with 2 faces.  There is no way to get a sum of 3.

# Example 5:
# Input: d = 30, f = 30, target = 500
# Output: 222616187
# Explanation: 
# The answer must be returned modulo 10^9 + 7.
 
# Constraints:
# 1 <= d, f <= 30
# 1 <= target <= 1000


def numRollsToTarget(d, f, target):
	"""
	:type d: int
	:type f: int
	:type target: int
	:rtype: int
	"""
	mod = 10**9 + 7
	dp = [[0 for i in range(target + 1)] for j in range(d + 1)]
	dp[0][0] = 1
	for i in range(1, d + 1):
		for j in range(1, f + 1):
			for k in range(j, target + 1):
				dp[i][k] = (dp[i][k] + dp[i - 1][k - j]) % mod
	return dp[d][target]


assert numRollsToTarget(1, 6, 3)== 1
assert numRollsToTarget(2, 6, 7) == 6
assert numRollsToTarget(2, 5, 10)== 1
assert numRollsToTarget(1, 2, 3)== 0
assert numRollsToTarget(30, 30, 500)== 222616187
assert numRollsToTarget(3, 5, 6) == 10
assert numRollsToTarget(3, 5, 5) == 6
assert numRollsToTarget(3, 5, 4) == 3
