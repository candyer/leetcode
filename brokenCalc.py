# https://leetcode.com/problems/broken-calculator/description/


# 991. Broken Calculator


# On a broken calculator that has a number showing on its display, we can perform two operations:

# Double: Multiply the number on the display by 2, or;
# Decrement: Subtract 1 from the number on the display.
# Initially, the calculator is displaying the number X.

# Return the minimum number of operations needed to display the number Y.


# Example 1:
# Input: X = 2, Y = 3
# Output: 2
# Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.

# Example 2:
# Input: X = 5, Y = 8
# Output: 2
# Explanation: Use decrement and then double {5 -> 4 -> 8}.

# Example 3:
# Input: X = 3, Y = 10
# Output: 3
# Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.

# Example 4:
# Input: X = 1024, Y = 1
# Output: 1023
# Explanation: Use decrement operations 1023 times.
 
# Note:
# 1 <= X <= 10^9
# 1 <= Y <= 10^9


def brokenCalc(X, Y):
	"""
	:type X: int
	:type Y: int
	:rtype: int
	"""
	
	if X >= Y:
		return X - Y
	else:
		res = 0
		while Y > X:
			if Y % 2 != 0:
				Y += 1
			else:
				Y /= 2
			res += 1
			if Y < X:
				res += X - Y
				Y = X
		return res


assert brokenCalc(999999999, 1000000000) == 500000000
assert brokenCalc(7, 1000000000) == 40
assert brokenCalc(30, 42) == 10
assert brokenCalc(26, 49) == 3
assert brokenCalc(2, 3) == 2
assert brokenCalc(5, 8) == 2
assert brokenCalc(3, 10) == 3
assert brokenCalc(3, 49) == 10
assert brokenCalc(1024, 1) == 1023
assert brokenCalc(1024, 1024) == 0



