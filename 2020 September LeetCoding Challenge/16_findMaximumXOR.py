# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/556/week-3-september-15th-september-21st/3462/

# Maximum XOR of Two Numbers in an Array


# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.
# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
# Could you do this in O(n) runtime?

# Example:
# Input: [3, 10, 5, 25, 2, 8]
# Output: 28
# Explanation: The maximum result is 5 ^ 25 = 28.


# from typing import List
# def findMaximumXOR(nums: List[int]) -> int:
# 	n = len(nums)
# 	res = 1
# 	for i in range(n):
# 		for j in range(i + 1, n):
# 			res = max(res, nums[i] ^ nums[j])
# 			print(nums[i], nums[j], res)
# 	return res


from typing import List
def findMaximumXOR(nums: List[int]) -> int:
	res = 0
	for i in range(31, -1, -1):	
		res <<= 1 #res *= 2
		pre = {n >> i for n in nums} # for each given number, find the first 1, 2, 3, ..., 32 binary digits
		res += any(res ^ 1 ^ p in pre for p in pre) 
	return res

assert(findMaximumXOR([3, 10, 5, 25, 2, 8]) == 28)

# if x ^ y == z then x ^ z == y
#  3: 00011
# 10: 01010
#  5: 00101
# 25: 11001
#  2: 00010
#  8: 01000

# start from left:                                     res: 0
# ----------------------------------------------------------------------
# 1  bit: (0,     0,     0,     1,     0,     0)       res * 2 + 1 = 1
# 2 bits: (00,    01,    00,    11,    00,    01)      res * 2 + 1 = 3
# 3 bits: (000,   010,   001,   110,   000,   010)     res * 2 + 1 = 7
# 4 bits: (0001,  0101,  0010,  1100,  0001,  0100)    res * 2 + 0 = 14
# 5 bits: (00011, 01010, 00101, 11001, 00010, 01000)   res * 2 + 0 = 28


