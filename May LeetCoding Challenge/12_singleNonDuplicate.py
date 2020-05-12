# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3327/

# Single Element in a Sorted Array

# You are given a sorted array consisting of only integers where every element appears exactly twice, 
# except for one element which appears exactly once. Find this single element that appears only once.


# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2

# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10
 

# Note: Your solution should run in O(log n) time and O(1) space.

from typing import List
from collections import Counter

def singleNonDuplicate(nums: List[int]) -> int:
	return sum(set(nums)) * 2 - sum(nums)


def singleNonDuplicate(nums: List[int]) -> int:
	res = nums[0]
	for num in nums[1:]:
		res ^= num
	return res


def singleNonDuplicate(nums: List[int]) -> int:
	for k, v in Counter(nums).items():
		if v == 1:
			return k


def singleNonDuplicate(nums: List[int]) -> int:
	left, right = 0, len(nums) - 1
	while left < right:
		mid = (left + right) // 2
		if nums[mid] == nums[mid - 1]:
			if (mid - 1) % 2 != 0:
				right = mid - 2
			else:
				left = mid + 1
		elif nums[mid] == nums[mid + 1]:
			if (mid + 1) % 2 != 0:
				left = mid + 2
			else:
				right = mid - 1
		else:
			return nums[mid]
	return nums[left]

assert(singleNonDuplicate([1,1,2,3,3,4,4,8,8]) == 2)
assert(singleNonDuplicate([3,3,7,7,10,11,11]) == 10)


