# https://leetcode.com/problems/set-mismatch/description/

# 645. Set Mismatch

# The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, 
# one of the numbers in the set got duplicated to another number in the set, which results in 
# repetition of one number and loss of another number.

# Given an array nums representing the data status of this set after the error. Your task is 
# to firstly find the number occurs twice and then find the number that is missing. Return 
# them in the form of an array.

# Example 1:   Input: nums = [1,2,2,4]   Output: [2,3]

# Note:
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.

##########################
####### solution 1 #######
##########################
from collections import Counter as c
def findErrorNums(nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	n = len(nums)
	count = c(nums)
	duplicate = missing = 0
	for i in range(1, n + 1):
		if count[i] > 1:
			duplicate = i
		if count[i] == 0:
			missing = i
	return [duplicate, missing]


##########################
####### solution 2 #######
##########################


def findErrorNums(nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	n = len(nums)
	espected_sum = n * (n + 1) / 2
	actual_sum = sum(nums)
	set_sum = sum(set(nums))
	duplicate = actual_sum - set_sum
	missing = espected_sum - set_sum
	return [duplicate, missing]

assert findErrorNums([1,2,2,4]) == [2,3]
assert findErrorNums([1,2,4,5,1]) == [1,3]
