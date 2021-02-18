# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3643/

# Container With Most Water

# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Example 3:
# Input: height = [4,3,2,1,4]
# Output: 16

# Example 4:
# Input: height = [1,2,1]
# Output: 2
 
# Constraints:
# n == height.length
# 2 <= n <= 3 * 10^4
# 0 <= height[i] <= 3 * 10^4


from typing import List
def maxArea(height: List[int]) -> int:
	n = len(height)
	area, l, r = 0, 0, n - 1
	while l < r:
		area = max(area, min(height[l], height[r]) * (r - l))
		if height[l] < height[r]:
			l += 1
		else:
			r -= 1
	return area

assert(maxArea([1,8,6,2,5,4,8,3,7]) == 49)
assert(maxArea([1,1]) == 1)
assert(maxArea([4,3,2,1,4]) == 16)
assert(maxArea([1,2,1]) == 2)










