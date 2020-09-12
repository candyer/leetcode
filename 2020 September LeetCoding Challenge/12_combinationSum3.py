# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3457/

# Combination Sum III

# Find all possible combinations of k numbers that add up to a number n, given that only numbers 
# from 1 to 9 can be used and each combination should be a unique set of numbers.

# Note:
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.

# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]

# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]



from typing import List
from itertools import combinations
##############################################################
def combinationSum3(k: int, n: int) -> List[List[int]]:
	res = []
	for item in combinations(range(1, 10), k):		
		if sum(item) == n:
			res.append(item)
	return res   




##############################################################
def rec(candidates, k, new_sum, path, res):
	if k < 0 or new_sum < 0:
		return 
	if k == 0 and new_sum == 0:
		res.append(path)
	for i in range(len(candidates)):
		rec(candidates[i + 1:], k - 1, new_sum - candidates[i], path + [candidates[i]], res)

def combinationSum3(k: int, n: int) -> List[List[int]]:
	res = []
	rec(range(1, 10), k, n, [], res) # candidates, k, n, path, result
	return res



assert(combinationSum3(3, 7) == [[1, 2, 4]])
assert(combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]])
assert(combinationSum3(10, 36) == [])

