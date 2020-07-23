# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3399/

# Single Number III

# Given an array of numbers nums, in which exactly two elements appear only once and all 
# the other elements appear exactly twice. Find the two elements that appear only once.

# Example:
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# Note:

# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. 
# Could you implement it using only constant space complexity?

from collections import Counter
from typing import List
def singleNumber(nums: List[int]) -> List[int]:
	res = []
	for k, v in Counter(nums).items():
		if v == 1:
			res.append(k)
	return res


def singleNumber(nums: List[int]) -> List[int]:
	res = set()
	for i in nums:
		if i in res:
			res.discard(i)
		else:
			res.add(i)
	return list(res)


def singleNumber(nums: List[int]) -> List[int]:
	xor = 0
	for num in nums:
		xor ^= num
	xor &= -xor
	a = b = 0
	for num in nums:
		if num & xor:
			a ^= num
		else:
			b ^= num
	return [a, b]

assert(singleNumber([1,2,1,3,2,5,6,6]) == [3, 5])

