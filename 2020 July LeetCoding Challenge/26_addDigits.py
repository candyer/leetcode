# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3402/

# Add Digits

# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# Example:
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#              Since 2 has only one digit, return it.
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?

########################################################
def digit_sum(num: int) -> int:
    res = 0
    while num:
        digit = num % 10
        res += digit
        num //= 10
    return res

def addDigits(num: int) -> int:
    res = 0
    while num > 9:
        num = digit_sum(num)
        res += num
    return num




########################################################
def addDigits(num: int) -> int:
    '''https://en.wikipedia.org/wiki/Digital_root#Congruence_formula'''
    if num == 0:
        return 0
    return (num - 1) % 9 + 1

assert(addDigits(38) == 2)
assert(addDigits(21) == 3)
assert(addDigits(0) == 0)
assert(addDigits(146) == 2)



