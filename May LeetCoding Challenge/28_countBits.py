# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3343/

# Counting Bits

# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num 
# calculate the number of 1's in their binary representation and return them as an array.


# Example 1:
# Input: 2
# Output: [0,1,1]

# Example 2:
# Input: 5
# Output: [0,1,1,2,1,2]
# Follow up:

# It is very easy to come up with a solution with run time O(n*sizeof(integer)). 
# But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function 
# like __builtin_popcount in c++ or in any other language.


from typing import List
def countBits(num: int) -> List[int]:
	return [bin(i).count('1') for i in range(num + 1)]
	

from typing import List
def countBits(num: int) -> List[int]:
	dp = [0] * (num + 1)
	for i in range(1, num + 1):
		tmp = 0
		if i % 2:
			tmp = 1
		dp[i] = dp[i // 2] + tmp
	return dp

assert(countBits(2) == [0,1,1])
assert(countBits(5) == [0,1,1,2,1,2])
assert(countBits(11) == [0,1,1,2,1,2,2,3,1,2,2,3])




