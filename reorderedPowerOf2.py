# https://leetcode.com/problems/reordered-power-of-2/description/

# 869. Reordered Power of 2

# Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading 
# digit is not zero.Return true if and only if we can do this in a way such that the resulting number is a power of 2.

# Example 1:
# Input: 1
# Output: true

# Example 2:
# Input: 10
# Output: false

# Example 3:
# Input: 16
# Output: true

# Example 4:
# Input: 24
# Output: false

# Example 5:
# Input: 46
# Output: true
 
# Note:
# 1 <= N <= 10^9

from collections import Counter as c
def reorderedPowerOf2(N):
	"""
	:type N: int
	:rtype: bool
	"""
	return c(str(N)) in [c(str(2**i)) for i in range(31)]
	



assert reorderedPowerOf2(1) == True
assert reorderedPowerOf2(10) == False
assert reorderedPowerOf2(16) == True
assert reorderedPowerOf2(24) == False
assert reorderedPowerOf2(46) == True
assert reorderedPowerOf2(2410) == True
assert reorderedPowerOf2(10**9) == False
assert reorderedPowerOf2(125368709) == True
assert reorderedPowerOf2(1073741824) == True





