# https://leetcode.com/problems/rotate-array/description/

# 189. Rotate Array

# Rotate an array of n elements to the right by k steps.

# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

# Could you do it in-place with O(1) extra space?

def rotate(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	#solution 1
	n = len(nums)
	tmp = nums[:]
	for i in range(n):
		nums[i] = tmp[(n - k + i) % n ]


	#solution 2	
	n = len(nums)
	nums[:] = nums[n - k :] + nums[: n - k]

print rotate([1,2,3,4,5,6,7], 3) #[5, 6, 7, 1, 2, 3, 4]
print rotate([1,2,3,4,5], 4) #[2, 3, 4, 5, 1]


