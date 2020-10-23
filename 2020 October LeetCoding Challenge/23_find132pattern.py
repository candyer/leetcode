# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3505/


# 132 Pattern


# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], 
# nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return false.
# Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?



# Example 1:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.

# Example 2:
# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

# Example 3:
# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

# Constraints:
# n == nums.length
# 1 <= n <= 10^4
# -109 <= nums[i] <= 10^9

from typing import List
def find132pattern(nums: List[int]) -> bool:
	n = len(nums)
	if n < 3:
		return False
	two = float('-inf') # two means 2 in 132
	stack = []
	for i in range(n - 1, -1, -1):
		if nums[i] >= two:
			while stack and stack[-1] < nums[i]:
				two = stack.pop()
		else:
			return True
		stack.append(nums[i])
	return False

assert(find132pattern([1,2,3,4]) == False)
assert(find132pattern([3,1,4,2]) == True)
assert(find132pattern([-1,3,2,0]) == True)
assert(find132pattern([4, 3, 2, 1]) == False)












