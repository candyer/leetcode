# https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/

# 915. Partition Array into Disjoint Intervals

# Given an array A, partition it into two (contiguous) subarrays left and right so that:

# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
# Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.



# Example 1:
# Input: [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]

# Example 2:
# Input: [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]

# Note:
# 2 <= A.length <= 30000
# 0 <= A[i] <= 10^6
# It is guaranteed there is at least one way to partition A as described.


def partitionDisjoint(A):
	"""
	:type A: List[int]
	:rtype: int
	"""
	n = len(A)

	maxi = A[0]
	max_left = [0]* n
	for i in range(n):
		maxi = max(maxi, A[i])
		max_left[i] = maxi

	mini = A[-1]
	min_right = [float('inf')] * n
	for i in range(n - 1, -1, -1):
		mini = min(mini, A[i])
		min_right[i] = mini

	for i in range(n):
		if max_left[i] <= min_right[i + 1]:
			return i + 1


assert partitionDisjoint([0,1]) == 1
assert partitionDisjoint([0,0,1]) == 1
assert partitionDisjoint([0,0]) == 1
assert partitionDisjoint([5,5,6,6,9,7,5]) == 1
assert partitionDisjoint([9,8,7,6,10]) == 4
assert partitionDisjoint([5,6,7,4,10,9]) == 4
assert partitionDisjoint([5,0,3,8,6]) == 3
assert partitionDisjoint([1,1,1,0,6,12]) == 4





