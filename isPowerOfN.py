#leetcode 231 -- Power of Two
#Given an integer, write a function to determine if it is a power of two.
def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    ## solution 1
    if n <= 0:  return False
    while n % 2 == 0:
        n /= 2
    return n == 1

    ## solution 2
    if n <= 0:  return False
    if n == 1:  return True
    while n > 1:
        if n == 2:  return True
        if n % 2 != 0:  return False
        n /= 2



# leetcode 326 - Power of Three
# Given an integer, write a function to determine if it is a power of three.
def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    ## solution 1
    if n <= 0:  return False
    while n % 3 == 0:
        n /= 3
    return n == 1

    ## solution 2
    if n <= 0:  return False
    if n == 1:  return True
    while n > 1:
        if n == 3:
            return True
        if n % 3 != 0:
            return False
        n /= 3


# leetcode 342 - Power of Four
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
# Example: Given num = 16, return true. Given num = 5, return false.
def isPowerOfFour(n):
    """
    :type n: int
    :rtype: bool
    """
    ## solution 1
    if n <= 0:  return False
    while n % 4 == 0:
        n /= 4
    return n == 1

    ## solution 2
    if n <= 0:  return False
    if n == 1:  return True
    while n > 1:
        if n == 4:  return True
        if n % 4 != 0:  return False
        n /= 4


def isPowerofN1(m, n):
    """ both m and n are integers. n > 1.   return True if m if power of n, False otherwise """
    assert n > 1
    if m <= 0:  return False
    if m == 1:  return True
    while m > 1:
        if m == n:
            return True
        if m % n != 0:
            return False
        m /= n

def isPowerofN2(m, n):
    """ both m and n are integers. n > 1.   return True if m if power of n, False otherwise """
    assert n > 1
    if m <= 0:  return False
    while m % n == 0:
        m /= n
    return m == 1





