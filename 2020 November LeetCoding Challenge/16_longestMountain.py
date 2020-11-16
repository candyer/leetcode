# https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3533/

 # Longest Mountain in Array


# Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

# B.length >= 3
# There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# (Note that B could be any subarray of A, including the entire array A.)
# Given an array A of integers, return the length of the longest mountain. 
# Return 0 if there is no mountain.


# Example 1:
# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

# Example 2:
# Input: [2,2,2]
# Output: 0
# Explanation: There is no mountain.

# Note:
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000

# Follow up:
# Can you solve it using only one pass?
# Can you solve it in O(1) space?

from typing import List
def longestMountain(A: List[int]) -> int:
	n = len(A)
	left = res = 0
	while left < n:
		right = left
		if right + 1 < n and A[right] < A[right + 1]:
			while right + 1 < n and A[right] < A[right + 1]: #upward
				right += 1
			if right + 1 < n and A[right] > A[right + 1]: 
				while right + 1 < n and A[right] > A[right + 1]: #downward
					right += 1
				res = max(res, right - left + 1)
		left = max(right, left + 1)
	return res

assert(longestMountain([2,1,4,7,3,2,5]) == 5)
assert(longestMountain([2,2,2]) == 0)
assert(longestMountain([2,2,2,3]) == 0)
assert(longestMountain([2,2,2,3,2]) == 3)
assert(longestMountain([6,1,7,10]) == 0)
assert(longestMountain([10,3,5,3,5]) == 3) 
assert(longestMountain([8,3,2,5,10,5,3,6,2]) == 5)
assert(longestMountain([1,1,2,3,4,4,3,3,1,7]) == 0)




