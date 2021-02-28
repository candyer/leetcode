# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3654/

# Divide Two Integers


# Given two integers dividend and divisor, divide two integers without using multiplication, 
# division, and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero, which means losing its fractional part. 
# For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

# Note:
# Assume we are dealing with an environment that could only store integers within the 32-bit 
# signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 
# 2^31 − 1 when the division result overflows.
 
# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = truncate(3.33333..) = 3.

# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = truncate(-2.33333..) = -2.

# Example 3:
# Input: dividend = 0, divisor = 1
# Output: 0

# Example 4:
# Input: dividend = 1, divisor = 1
# Output: 1
 
# Constraints:
# -2^31 <= dividend, divisor <= 2^31 - 1
# divisor != 0


from math import ceil, floor
def divide(dividend: int, divisor: int) -> int:
    if dividend == -2147483648 and divisor == -1:
        return 2147483647
    flag = (dividend > 0) != (divisor > 0)
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        tmp, i = divisor, 1
        while dividend >= tmp:
            dividend -= tmp
            res += i
            i *= 2
            tmp *= 2    
    if flag:
        res = -res
    return res


assert(divide(10, 3) == 3)
assert(divide(7, -3) == -2)
assert(divide(0, 1) == 0)
assert(divide(1, 1) == 1)
assert(divide(-7, 3) == -2)
assert(divide(-100, 3) == -33)
assert(divide(-2147483648, 1) == -2147483648)
assert(divide(-1, -1) == 1)


