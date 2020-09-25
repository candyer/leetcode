# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3472/

# Largest Number


# Given a list of non negative integers, arrange them such that they form the largest number.

# Example 1:
# Input: [10,2]
# Output: "210"

# Example 2:
# Input: [3,30,34,5,9]
# Output: "9534330"
# Note: The result may be very large, so you need to return a string instead of an integer.

from functools import cmp_to_key
from typing import List
def largestNumber(nums: List[int]) -> str:
	nums = sorted(map(str, nums), key=cmp_to_key(lambda a, b: [1, -1][a + b > b + a]))
	res = ''.join(nums).lstrip('0')
	return res or '0'



assert(largestNumber([0, 0, 0]) == '0')
assert(largestNumber([10,2]) == '210')
assert(largestNumber([3,30,34,5,9]) == '9534330')
assert(largestNumber([325,3,34,5,9]) == "95343325")
assert(largestNumber([345,3,325,5,9]) == "953453325")






