# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3510/

# Summary Ranges


# You are given a sorted unique integer array nums.
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
# That is, each element of nums is covered by exactly one of the ranges, and there is no integer x
# such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
 

# Example 1:
# Input: nums = [0,1,2,4,5,7]      Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"

# Example 2:
# Input: nums = [0,2,3,4,6,8,9]      Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"

# Example 3:
# Input: nums = []      Output: []

# Example 4:
# Input: nums = [-1]      Output: ["-1"]

# Example 5:
# Input: nums = [0]      Output: ["0"]
 

# Constraints:
# 0 <= nums.length <= 20
# -2^31 <= nums[i] <= 2^31 - 1
# All the values of nums are unique.


from typing import List
def summaryRanges(nums: List[int]) -> List[str]:
	nums.append('*')
	res, pre = [], nums[0]
	for i in range(1, len(nums)):
		if nums[i - 1] + 1 != nums[i]:
			if pre == nums[i - 1]:
				res.append(str(pre))
			else:
				res.append("{}->{}".format(pre, nums[i - 1]))
			pre = nums[i]
	return res



assert(summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"])
assert(summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"])
assert(summaryRanges([]) == [])
assert(summaryRanges([-1]) == ["-1"])
assert(summaryRanges([0]) == ["0"])
assert(summaryRanges([-10, -2, 0, 1, 3, 5]) == ['-10', '-2', '0->1', '3', '5'])







