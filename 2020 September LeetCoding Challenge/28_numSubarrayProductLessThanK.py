# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3475/


# Subarray Product Less Than K


# Your are given an array of positive integers nums.
# Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

# Example 1:
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

# Note:
# 0 < nums.length <= 50000.
# 0 < nums[i] < 1000.
# 0 <= k < 10^6.



from typing import List
def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
	if k <= 1:
		return 0
	res, left, prod = 0, 0, 1
	for right, num in enumerate(nums):
		prod *= num
		while prod >= k and left < len(nums):
			prod //= nums[left]
			left += 1
		res += right - left + 1
	return res


assert(numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8)
assert(numSubarrayProductLessThanK([1, 2, 3], 1) == 0)
assert(numSubarrayProductLessThanK([1, 2, 3, 4, 5], 0) == 0)
