# https://leetcode.com/problems/container-with-most-water/description/

# 11. Container With Most Water
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, 
# which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.


# Example:
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

###########################
## Brute Force O(n^2) TLE##
###########################
def maxArea(height):
	"""
	:type height: List[int]
	:rtype: int
	"""
	max_area = 0
	n = len(height)
	for i in range(n):
		for j in range(i + 1, n):
			max_area = max(max_area, (j - i) * min(height[i], height[j]))
	return max_area


###########################
### two pointers O(n) AC ##
###########################
def maxArea(height):
	"""
	:type height: List[int]
	:rtype: int
	"""
	n = len(height)
	max_area, start, end = 0, 0, n - 1
	while start < end:
		max_area = max(max_area, (end - start) * min(height[start], height[end]))
		if height[start] < height[end]:
			start += 1
		else:
			end -= 1
	return max_area


assert maxArea([8, 3, 12, 8]) == 24
assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert maxArea(range(10**6)) == 249999500000

