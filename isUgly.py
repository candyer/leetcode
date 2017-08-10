# Leetcode 263 -- Ugly Number
# https://leetcode.com/problems/ugly-number/description/

# Write a program to check whether a given number is an ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
#For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
# Note that 1 is typically treated as an ugly number.



def isUgly(num):
    """
    :type num: int
    :rtype: bool
    """
    if num <= 0:
        return False
    for x in [2, 3, 5]:
        while num % x == 0:
            num /= x
    return num == 1

print isUgly(1200)


assert isUgly(1) == True
assert isUgly(6) == True
assert isUgly(6) == True
assert isUgly(14) == False
assert isUgly(-34567) == False
assert isUgly(0) == False 
assert isUgly(7) == False 
assert isUgly(30) == True
