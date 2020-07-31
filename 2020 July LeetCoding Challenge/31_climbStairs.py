# https://leetcode.com/explore/featured/card/july-leetcoding-challenge/548/week-5-july-29th-july-31st/3407/

# Climbing Stairs

# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# Example 1:
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:
# 1 <= n <= 45

def climbStairs(n: int) -> int:
	'''fibonacci number'''
	arr = [1, 1]
	a = b = 1
	for i in range(n - 1):
		a, b = b, a + b
	return b
assert(climbStairs(2) == 2)
assert(climbStairs(5) == 8)
assert(climbStairs(13) == 377)
assert(climbStairs(40) == 165580141)

