# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3521/

# Find the Smallest Divisor Given a Threshold


# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and 
# divide all the array by it and sum the result of the division. Find the smallest divisor such that the 
# result mentioned above is less than or equal to threshold.

# Each result of division is rounded to the nearest integer greater than or equal to that element. 
# (For example: 7/3 = 3 and 10/2 = 5).

# It is guaranteed that there will be an answer.


# Example 1:
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
# If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 

# Example 2:
# Input: nums = [2,3,5,7,11], threshold = 11
# Output: 3

# Example 3:
# Input: nums = [19], threshold = 5
# Output: 4
 

# Constraints:
# 1 <= nums.length <= 5 * 10^4
# 1 <= nums[i] <= 10^6
# nums.length <= threshold <= 10^6

from typing import List
from math import ceil
def sum_arr(nums: List[int], threshold: int) -> int:
	total = 0
	for num in nums:
		total += ceil(num / threshold)
	return total

def smallestDivisor(nums: List[int], threshold: int) -> int:
	l, r = 1, max(nums)
	while l < r:
		divisor = (l + r) // 2
		total = sum_arr(nums, divisor)
		if total > threshold:
			l = divisor + 1
		else:
			r = divisor
	return l

assert(smallestDivisor([1,2,5,9], 6) == 5)
assert(smallestDivisor([2,3,5,7,11], 11) == 3)
assert(smallestDivisor([19], 5) == 4)
assert(smallestDivisor([18, 3, 5, 17, 13, 23], 15) == 6)




