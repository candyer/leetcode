# https://leetcode.com/problems/beautiful-arrangement/description/

# 526. Beautiful Arrangement

# Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed 
# by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
# Now given N, how many beautiful arrangements can you construct?

# Example 1:
# Input: 2
# Output: 2
# Explanation: 

# The first beautiful arrangement is [1, 2]:

# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

# The second beautiful arrangement is [2, 1]:

# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
# Note:
# N is a positive integer and will not exceed 15.



##########################
##### solution 1 #########
##########################

def countArrangement(N):
	"""
	:type N: int
	:rtype: int
	"""
	memo = {}

	def helper(size, nums):
		if size == 1:
			return 1
		key = nums
		if key in memo:
			return memo[key]
		res = 0

		for i in range(len(nums)):
			if size % nums[i] == 0 or nums[i] % size == 0:
				res += helper(size - 1, nums[:i] + nums[i + 1:])
		memo[key] = res
		return res

	return helper(N, tuple(range(1, N + 1)))


##########################
##### solution 2 #########
##########################

# def countArrangement(N):
# 	"""
# 	:type N: int
# 	:rtype: int
# 	"""
# 	res = [1, 1, 2, 3, 8, 10, 36, 41, 132, 250, 700, 750, 4010, 4237, 10680, 24679]
# 	return res[N]   


print countArrangement(4) == 8






