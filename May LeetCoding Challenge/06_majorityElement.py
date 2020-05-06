# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/

# Given an array of size n, find the majority element. 
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist 
# in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2

from collections import Counter
from typing import List
def majorityElement(nums: List[int]) -> int:
	d = Counter(nums)
	return max(d, key=d.get)


def majorityElement(nums: List[int]) -> int:
	return sorted(nums)[len(nums) // 2]

assert(majorityElement([3,2,3]) == 3)
assert(majorityElement([2,2,1,1,1,2,2]) == 2)
assert(majorityElement([6,1,1,1]) == 1)
