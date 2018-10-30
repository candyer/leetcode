# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/

# 453. Minimum Moves to Equal Array Elements

# Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, 
# where a move is incrementing n - 1 elements by 1.

# Example:

# Input:
# [1,2,3]

# Output:
# 3

# Explanation:
# Only three moves are needed (remember each move increments two elements):

# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]


def minMoves(nums):
	"""
	:type nums: List[int]
	:rtype: int

	define x moves needed to fit the requirement;
	define y is the final value for every number after x momves;
	define n is the length of the list;
	defind mini is the smallest number in the original list;
	define origin_sum is the original sum before any moves.

	origin_sum + x * (n - 1) = y * n
	and y = mini + x

	> origin_sum + x * (n - 1) = ( mini + x) * n
	> origin_sum + x * n - x = mini * n + x * n
	> origin_sum - x = mini * n 
	> x = origin_sum - mini * n
	"""
	return sum(nums) - min(nums) * len(nums)


assert minMoves([1,2,3]) == 3
assert minMoves([2,5,6]) == 7
assert minMoves([4,4,6]) == 2