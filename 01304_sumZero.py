# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/

# 1304. Find N Unique Integers Sum up to Zero

# Given an integer n, return any array containing n unique integers such that they add up to 0.

# Example 1:
# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

# Example 2:
# Input: n = 3
# Output: [-1,0,1]

# Example 3:
# Input: n = 1
# Output: [0]

# Constraints:
# 1 <= n <= 1000

from typing import List
def sumZero1(n: int) -> List[int]:
	res = []
	if n % 2:
		res.append(0)
	for i in range(1, n // 2 + 1):
		res.append(i)
		res.append(-i)
	return res


def sumZero2(n: int) -> List[int]:
	res = []
	for i in range(n - 1):
		res.append(i)
	res.append(-sum(res))
	return res


assert(sumZero1(1) == [0])
assert(sumZero1(3) == [0, 1, -1])
assert(sumZero1(5) == [0, 1, -1, 2, -2])
assert(sumZero1(10) == [1, -1, 2, -2, 3, -3, 4, -4, 5, -5])

assert(sumZero2(1) == [0])
assert(sumZero2(3) == [0, 1, -1])
assert(sumZero2(5) == [0, 1, 2, 3, -6])
assert(sumZero2(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, -36])



