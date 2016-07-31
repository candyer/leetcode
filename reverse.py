# https://leetcode.com/problems/reverse-integer/

# leetcode 7 --- Reverse Integer

#Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321
# Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, 
# then the reverse of 1000000003 overflows. How should you handle such cases?
# For the purpose of this problem, 
# assume that your function returns 0 when the reversed integer overflows.

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    y = abs(x)
    res = 0
    while y != 0:
        res = res * 10 + y % 10
        y /= 10
        
    if res > 2**31:
        return 0
    if x < 0:
        return -res
    return res
    
    
# print reverse(123) #321
# print reverse(1000000003) #0
# print reverse(3000000001) #1000000003
# print reverse(-1000000003) #0
# print reverse(-3000000001) #-1000000003
# print reverse(-123) #-321
# print reverse(0) #0
# print reverse(1534236469) #0
# print reverse(-1534236469) #0
