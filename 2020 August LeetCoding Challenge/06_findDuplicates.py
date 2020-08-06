# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3414/

# Find All Duplicates in an Array

# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]


######### time:O(n)  space:O(n) ########
from typing import List
def findDuplicates(nums: List[int]) -> List[int]:
	count = {}
	res = []
	for num in nums:
		if num not in count:
			count[num] = 1
		else:
			res.append(num)
	return res


######### time:O(n)  space:O(1) ########
def findDuplicates(nums: List[int]) -> List[int]:
	res = []
	for num in nums:
		pos = abs(num) - 1
		if nums[pos] < 0:
			res.append(pos + 1)
		nums[pos] *= -1
	return res

assert(findDuplicates([4,3,2,7,8,2,3,1]) == [2, 3])
assert(findDuplicates([1,2,1,5,5,6,6,8]) == [1, 5, 6])

