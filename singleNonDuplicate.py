# https://leetcode.com/problems/single-element-in-a-sorted-array/#/description

#similar to problme No.136 -- Single Number
# Given a sorted array consisting of only integers where every element appears twice 
# except for one element which appears once. Find this single element that appears only once.

# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2

# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10
# Note: Your solution should run in O(log n) time and O(1) space.

def singleNonDuplicate(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	left, right = 0, len(nums) - 1
	while left < right:
		mid = (left + right) / 2
		if nums[mid] == nums[mid - 1]:
			if (mid - 1) % 2 != 0:
				right = mid - 2
			else:
				left = mid + 1
		elif nums[mid] == nums[mid + 1]:
			if (mid + 1) % 2 != 0:
				left = mid + 2
			else:
				right = mid - 1
		else:
			return nums[mid]
	return nums[left]

print singleNonDuplicate([1,1,2,2,3,4,4,8,8]) #3
print singleNonDuplicate([1,1,2,3,3,4,4,8,8]) #2
print singleNonDuplicate([3,3,7,7,10,10,11]) #11
