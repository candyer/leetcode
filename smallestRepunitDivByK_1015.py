# https://leetcode.com/problems/smallest-integer-divisible-by-k/description/


# 1015. Smallest Integer Divisible by K


# Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K, 
# and N only contains the digit 1.

# Return the length of N.  If there is no such N, return -1.

# Example 1:
# Input: 1
# Output: 1
# Explanation: The smallest answer is N = 1, which has length 1.

# Example 2:
# Input: 2
# Output: -1
# Explanation: There is no such positive integer N divisible by 2.

# Example 3:
# Input: 3
# Output: 3
# Explanation: The smallest answer is N = 111, which has length 3.
 
# Note:
# 1 <= K <= 10^5

def smallestRepunitDivByK(K):
	"""
	:type K: int
	:rtype: int
	"""
	if K % 2 == 0 or K % 5 == 0:
		return -1

	remainder = 0
	remainders = set()
	for i in xrange(K):
		remainder *= 10
		remainder += 1
		remainder %= K
		if remainder == 0:
			return i + 1
		else:
			if remainder not in remainders:
				remainders.add(remainder)
			else:
				return -1


assert smallestRepunitDivByK(1) == 1
assert smallestRepunitDivByK(2) == -1
assert smallestRepunitDivByK(3) == 3
assert smallestRepunitDivByK(4) == -1
assert smallestRepunitDivByK(9) == 9
assert smallestRepunitDivByK(99) == 18
assert smallestRepunitDivByK(72) == -1
assert smallestRepunitDivByK(19927) == 19926




