# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3482/

# K-diff Pairs in an Array


# Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
# 0 <= i, j < nums.length
# i != j
# a <= b
# b - a == k

# Example 1:
# Input: nums = [3,1,4,1,5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.

# Example 2:
# Input: nums = [1,2,3,4,5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

# Example 3:
# Input: nums = [1,3,1,5,4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).

# Example 4:
# Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
# Output: 2

# Example 5:
# Input: nums = [-1,-2,-3], k = 1
# Output: 2

# Constraints:
# 1 <= nums.length <= 10^4
# -10^7 <= nums[i] <= 10^7
# 0 <= k <= 10^7



from typing import List
from collections import Counter
def findPairs(nums: List[int], k: int) -> int:
	counter = Counter(nums)
	res = 0
	for num in set(nums):
		if k > 0 and num + k in counter:
			res += 1
		if k == 0 and counter[num] > 1:
			res += 1
	return res


assert(findPairs([3,1,4,1,5], 2) == 2)
assert(findPairs([1,2,3,4,5], 1) == 4)
assert(findPairs([1,3,1,5,4], 0) == 1)
assert(findPairs([1,2,4,4,3,3,0,9,2,3], 3) == 2)
assert(findPairs([-1,-2,-3], 1) == 2)






