# https://leetcode.com/problems/numbers-with-same-consecutive-differences/


# 967. Numbers With Same Consecutive Differences


# Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.
# Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 
# 01 has one leading zero and is invalid, but 0 is valid.
# You may return the answer in any order.


# Example 1:
# Input: N = 3, K = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.

# Example 2:
# Input: N = 2, K = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
 
# Note:
# 1 <= N <= 9
# 0 <= K <= 9


def numsSameConsecDiff(N, K):
	"""
	:type N: int
	:type K: int
	:rtype: List[int]
	"""
	res = {i for i in range(1, 10)}
	for _ in range(N - 1):
		tmp = set()
		for num in res:
			a = num % 10
			if a + K <= 9:
				tmp.add(num * 10 + a + K)
			if a - K >= 0:
				tmp.add(num * 10 + a - K)
		res = tmp
	if N == 1:
		res.add(0)
	return list(res)


# print numsSameConsecDiff(1, 1) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print numsSameConsecDiff(4, 1)
# print numsSameConsecDiff(3, 0)
# print numsSameConsecDiff(9, 0)
# print numsSameConsecDiff(1, 8)
# print numsSameConsecDiff(3, 7)
# print numsSameConsecDiff(2, 1)
# print numsSameConsecDiff(6, 3)
# print numsSameConsecDiff(4, 0) == [7777, 3333, 6666, 2222, 9999, 5555, 1111, 8888, 4444]

