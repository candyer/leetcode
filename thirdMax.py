# https://leetcode.com/problems/third-maximum-number/description/


# 414. Third Maximum Number

# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, 
# return the maximum number. The time complexity must be in O(n).

# Example 1:
# Input: [3, 2, 1]
# Output: 1

# Explanation: The third maximum is 1.

# Example 2:
# Input: [1, 2]
# Output: 2

# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

# Example 3:
# Input: [2, 2, 3, 1]
# Output: 1

# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.



from collections import Counter as c
def thirdMax(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	d = c(nums)
	key = d.keys()
	n = len(key)
	if n < 3:
		return max(key)
	maxi1, maxi2, maxi3 = key[0], float('-inf'), float('-inf')
	for num in key[1:]:
		if num > maxi1:
			maxi3 = maxi2
			maxi2 = maxi1
			maxi1 = num

		elif num > maxi2:
			maxi3 = maxi2
			maxi2 = num
		elif num > maxi3:
			maxi3 = num
	return maxi3

assert thirdMax([-3, -2, -1]) == -3 
assert thirdMax([3, 2, 1]) == 1
assert thirdMax([1, 2]) == 2
assert thirdMax([2, 2, 3, 1]) == 1


