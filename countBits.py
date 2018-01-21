# https://leetcode.com/problems/counting-bits/description/

# 338. Counting Bits

# Given a non negative integer number num. For every numbers i in the 
# range 0 <= i <= num calculate the number of 1's in their binary representation 
# and return them as an array.

# Example: For num = 5 you should return [0,1,1,2,1,2].

# Follow up:
# It is very easy to come up with a solution with run time O(n*sizeof(integer)). 
# But can you do it in linear time O(n) /possibly in a single pass?

# Space complexity should be O(n).

# Can you do it like a boss? Do it without using any builtin function 
# like __builtin_popcount in c++ or in any other language.



def countBits(num):
	"""
	:type num: int
	:rtype: List[int]
	"""
	res = []
	for i in range(num + 1):
		tmp = bin(i)[2:].count('1')
		res.append(tmp)
	return res


def countBits1(num):
	"""
	:type num: int
	:rtype: List[int]
	"""
	dp = [0] * (num + 1)
	tmp = 1
	for i in range(1, num + 1):
		if tmp * 2 == i:
			tmp *= 2
		dp[i] = dp[i - tmp] + 1
	return dp

assert countBits1(5) == [0, 1, 1, 2, 1, 2]


