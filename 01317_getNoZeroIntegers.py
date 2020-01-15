# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/description/

# 1317. Convert Integer to the Sum of Two No-Zero Integers

# Given an integer n. No-Zero integer is a positive integer 
# which doesn't contain any 0 in its decimal representation.
# Return a list of two integers [A, B] where:
# A and B are No-Zero integers.
# A + B = n
# It's guarateed that there is at least one valid solution. 
# If there are many valid solutions you can return any of them.

# Example 1:
# Input: n = 2
# Output: [1,1]
# Explanation: A = 1, B = 1. A + B = n and both A and B don't contain any 0 in their decimal representation.

# Example 2:
# Input: n = 11
# Output: [2,9]

# Example 3:
# Input: n = 10000
# Output: [1,9999]

# Example 4:
# Input: n = 69
# Output: [1,68]

# Example 5:
# Input: n = 1010
# Output: [11,999]
 

# Constraints:
# 2 <= n <= 10^4


from typing import List

def is_0_inside(n: int) -> bool:
	if '0' in str(n):
		return False
	return True


def getNoZeroIntegers(n: int) -> List[int]:
	for i in range(1, n // 2 + 1):
		if is_0_inside(i) and is_0_inside(n - i):
			return [i, n - i]

assert(getNoZeroIntegers(2) == [1, 1])
assert(getNoZeroIntegers(11) == [2, 9])
assert(getNoZeroIntegers(10000) == [1, 9999])
assert(getNoZeroIntegers(69) == [1, 68])
assert(getNoZeroIntegers(1010) == [11, 999])
assert(getNoZeroIntegers(9999) == [1, 9998])
assert(getNoZeroIntegers(2001) == [2, 1999])
assert(getNoZeroIntegers(100) == [1, 99])


