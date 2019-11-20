# https://leetcode.com/problems/greatest-sum-divisible-by-three/description/


# 1262. Greatest Sum Divisible by Three

# Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that 
# it is divisible by three.


# Example 1:
# Input: nums = [3,6,5,1,8]
# Output: 18
# Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).

# Example 2:
# Input: nums = [4]
# Output: 0
# Explanation: Since 4 is not divisible by 3, do not pick any number.

# Example 3:
# Input: nums = [1,2,3,4,4]
# Output: 12
# Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
 

# Constraints:
# 1 <= nums.length <= 4 * 10^4
# 1 <= nums[i] <= 10^4

#######################################################################
from typing import List
def maxSumDivThree(nums: List[int]) -> int:
	n = len(nums)
	dp = [[0 for j in range(n)] for i in range(3)]
	dp[nums[0] % 3][0] = nums[0]
	for i in range(1, n):
		for j in range(3):
			pos = (j - nums[i]) % 3
			tmp = dp[pos][i - 1] + nums[i]
			if tmp % 3 == j:
				dp[j][i] = max(dp[j][i - 1], tmp)
			else:
				dp[j][i] = dp[j][i - 1]
	return dp[0][-1]


#######################################################################
from typing import List
def maxSumDivThree1(nums: List[int]) -> int:
	s = [0, 0, 0]
	for num in nums:
		for i in s[:]:
			s[(num + i) % 3] = max(s[(num + i) % 3], i + num)
	return s[0]


#######################################################################
from typing import List
def maxSumDivThree(nums: List[int]) -> int:
	total = sum(nums)
	remainder = total % 3
	if remainder == 0:
		return total

	nums.sort()
	one, two = [], []
	for num in nums:
		remainder1 = num % 3
		if remainder1 == 1:
			one.append(num)
		elif remainder1 == 2:
			two.append(num)

		if len(one) >= 2 and len(two) >= 2:
			break
			
	tmp1 = tmp2 = float('inf')
	if remainder == 1:
		if one:
			tmp1 = one[0]
		if len(two) > 1:
			tmp2 = two[0] + two[1]
	else:
		if len(one) > 1:
			tmp1 = one[0] + one[1]
		if two:
			tmp2 = two[0]
	return total - min(tmp1, tmp2)

assert(maxSumDivThree([3, 6, 5, 1, 8]) == 18)
assert(maxSumDivThree([4]) == 0)
assert(maxSumDivThree([1, 2, 3, 4, 4]) == 12)
assert(maxSumDivThree([1, 4]) == 0)
assert(maxSumDivThree([7, 9, 2, 10, 2, 8, 8]) == 42)
assert(maxSumDivThree([5, 5, 6]) == 6)
assert(maxSumDivThree([5, 2]) == 0)
assert(maxSumDivThree([5, 5, 3, 9, 6]) == 18)
assert(maxSumDivThree([9, 8, 5, 3]) == 12)
assert(maxSumDivThree([3, 9, 8, 10, 5, 2, 9]) == 39)
assert(maxSumDivThree([2, 8, 7, 2]) == 15)
assert(maxSumDivThree([9, 6, 8, 8, 8, 8, 9, 8]) == 48)
assert(maxSumDivThree([7, 10, 2, 3, 7, 2, 10, 5]) == 42)
assert(maxSumDivThree([3, 4, 3, 3, 1]) == 9)
assert(maxSumDivThree([3, 3, 3, 100]) == 9)
assert(maxSumDivThree([3, 4, 3, 3, 2]) == 15)



