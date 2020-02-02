# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

# 1281. Subtract the Product and Sum of Digits of an Integer

# Given an integer number n, return the difference between the product of its digits 
# and the sum of its digits.
 
# Example 1:
# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

# Example 2:
# Input: n = 4421
# Output: 21
# Explanation: 
# Product of digits = 4 * 4 * 2 * 1 = 32 
# Sum of digits = 4 + 4 + 2 + 1 = 11 
# Result = 32 - 11 = 21
 
# Constraints:
# 1 <= n <= 10^5


def subtractProductAndSum(n: int) -> int:
	prod = 1
	total = 0
	while n:
		digit = n % 10
		prod *= digit
		total += digit
		n //= 10
	return prod - total

assert(subtractProductAndSum(234) == 15)
assert(subtractProductAndSum(4421) == 21)
assert(subtractProductAndSum(10) == -1)

