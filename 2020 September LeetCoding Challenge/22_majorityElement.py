# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3469/

# Majority Element II

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# Note: The algorithm should run in linear time and in O(1) space.

# Example 1:
# Input: [3,2,3]
# Output: [3]

# Example 2:
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]



from typing import List
def majorityElement(nums: List[int]) -> List[int]:
	res = []
	min_count = len(nums) // 3
	for num in set(nums):
		if nums.count(num) > min_count:
			res.append(num)
	return res



from typing import List
def majorityElement(nums: List[int]) -> List[int]:
	'''there are at most two numbers fit this description'''
	num1 = num2 = '*'
	count1 = count2 = 0

	for num in nums:
		if num == num1:
			count1 += 1
		elif num == num2:
			count2 += 1
		elif count1 == 0:
			num1 = num
			count1 += 1
		elif count2 == 0:
			num2 = num
			count2 += 1
		else:
			count1 -= 1
			count2 -= 1

	res = []
	for num in [num1, num2]:
		if nums.count(num) > len(nums) // 3:
			res.append(num)
	return res


assert(majorityElement([3,2,3]) == [3])
assert(majorityElement([1,1,1,3,3,2,2,2]) == [1, 2])
assert(majorityElement([]) == [])
assert(majorityElement([1]) == [1])
assert(majorityElement([1,2]) == [1, 2])
assert(majorityElement([1, 2, 3, 4]) == [])
assert(majorityElement([1,1,3,3,2,2,2,1]) == [2, 1])

