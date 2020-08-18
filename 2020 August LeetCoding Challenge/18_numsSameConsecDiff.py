# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3428/

# Numbers With Same Consecutive Differences


# Return all non-negative integers of length N such that the absolute difference between every 
# two consecutive digits is K.

# Note that every number in the answer must not have leading zeros except for the number 0 itself. 
# For example, 01 has one leading zero and is invalid, but 0 is valid.

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

from typing import List
def numsSameConsecDiff(N: int, K: int) -> List[int]:
	res = set(range(1, 10))
	for i in range(N - 1):
		tmp = set()
		for num in res:
			last_digit = num % 10
			if last_digit + K <= 9:
				tmp.add(num * 10 + last_digit + K)
			if last_digit - K >= 0:
				tmp.add(num * 10 + last_digit - K)
		res = tmp
	if N == 1:
		res.add(0)
	return list(res)

assert(numsSameConsecDiff(3, 7) == [929, 707, 292, 818, 181])
assert(numsSameConsecDiff(2, 1) == [32, 65, 34, 67, 98, 10, 43, 12, 45, 78, 76, 21, 54, 23, 56, 89, 87])
