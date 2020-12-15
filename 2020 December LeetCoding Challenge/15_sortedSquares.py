# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3567/

# Squares of a Sorted Array


# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.


from typing import List
def sortedSquares(nums: List[int]) -> List[int]:
	''' Time Complexity: O(nlogn) '''
	return [num * num for num in sorted(nums, key=abs)]



def sortedSquares(nums: List[int]) -> List[int]:
	''' Time Complexity: O(nlogn) '''
	return sorted(num * num for num in nums)



def sortedSquares(nums: List[int]) -> List[int]:
	''' Time Complexity: O(n) '''
	n = len(nums)
	left, right, pos, res = 0, n - 1, n - 1, [0] * n
	while left <= right:
		if abs(nums[left]) < abs(nums[right]):
			res[pos] = nums[right] ** 2
			right -= 1
		else:
			res[pos] = nums[left] ** 2
			left += 1
		pos -= 1
	return res


assert(sortedSquares([-4,-1,0,3,10]) == [0, 1, 9, 16, 100])
assert(sortedSquares([-7,-3,2,3,11]) == [4, 9, 9, 49, 121])











