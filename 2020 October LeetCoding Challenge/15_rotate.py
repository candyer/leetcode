# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3496/

# Rotate Array

# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Follow up:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?
 


# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
 

# Constraints:
# 1 <= nums.length <= 2 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5

from typing import List

### Time Complexity: O(kn) ################################### 
### Space Complexity: O(1) ## 
def rotate(nums: List[int], k: int) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""
	n = len(nums)
	k %= n
	for i in range(k):
		tmp = nums[n - 1]
		for j in range(n - 1, 0, -1):
			nums[j] = nums[j - 1]
		nums[0] = tmp
		




### Time Complexity: O(n) #####################################  
### Space Complexity: O(n) ## 
def rotate(nums: List[int], k: int) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""
	n = len(nums)
	k %= n
	nums[:] = nums[-k:] + nums[:-k]
		




### Time Complexity: O(n) #####################################  
### Space Complexity: O(1) ## 
def reverse(nums, start, end):
	while start <= end:
		nums[start], nums[end] = nums[end], nums[start]
		start += 1
		end -= 1

def rotate(nums: List[int], k: int) -> None:
	"""
	Do not return anything, modify nums in-place instead.
	"""
	n = len(nums)
	k %= n
	reverse(nums, 0, n - 1);
	reverse(nums, 0, k - 1);
	reverse(nums, k, n - 1);






